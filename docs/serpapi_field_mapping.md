# SerpAPI Field Mapping Documentation

## Overview

This document maps the fields we need for lead generation to the actual fields available in SerpAPI's Google Local Results response.

## Actual SerpAPI Response Structure

Based on [SerpAPI Local Results documentation](https://serpapi.com/local-results), the `local_results` array contains objects with the following structure:

### Available Fields in `local_results` Items

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| `position` | int | Position in search results | `1` |
| `title` | string | Business name | `"Houndstooth Coffee"` |
| `rating` | float | Average rating | `4.6` |
| `reviews` | int | Number of reviews | `862` |
| `reviews_original` | string | Original reviews text | `"(862)"` |
| `price` | string | Price level | `"$$"` |
| `address` | string | Business address | `"401 Congress Ave. #100c"` |
| `type` | string | Business category/type | `"Coffee shop"` |
| `description` | string | Business description | `"Cozy hangout for carefully sourced brews"` |
| `place_id` | string | Google Place ID | `"11265938073076301333"` |
| `place_id_search` | string | SerpAPI search URL for this place | URL string |
| `lsig` | string | Google signature | `"AB86z5WAwZ6EQxM6P9ZAHqnLlPp2"` |
| `images` | array | Array of image URLs | `["https://..."]` |
| `links` | object | Contains phone, directions, website, order links | See below |
| `service_options` | object | Service options (dine_in, takeout, etc.) | `{"dine_in": true}` |
| `hours` | string | Operating hours | `"Open ⋅ Closes 6 PM"` |
| `gps_coordinates` | object | Latitude and longitude | `{"latitude": 30.2672, "longitude": -97.7431}` |

### Links Object Structure

The `links` object can contain:

```json
{
  "phone": "+15123946051",
  "directions": "https://maps.google.com/...",
  "website": "https://example.com",
  "order": "https://food.google.com/..."
}
```

**Note**: Not all businesses have all link types. The `website` field is optional.

## Field Mapping: What We Need vs. What's Available

### ✅ Fields Available Directly

| Our Field | SerpAPI Field | Notes |
|-----------|---------------|-------|
| `company_name` | `title` | Direct mapping |
| `website_url` | `links.website` | **Optional** - not all businesses have this |
| `phone` | `links.phone` | **Optional** - format: `"+15123946051"` |
| `location_city` | Extracted from `address` | Need to parse address string |
| `location_country` | From search `location` parameter | Not in individual result |
| `industry` | `type` | Direct mapping (e.g., "Coffee shop") |
| `description` | `description` | **Optional** - not all businesses have this |

### ❌ Fields NOT Available in Basic Response

| Our Field | Availability | Alternative Solution |
|-----------|--------------|---------------------|
| `employee_count` | **NOT AVAILABLE** | Would need Google Places API or web scraping |
| `decision_maker_name` | **NOT AVAILABLE** | Would need LinkedIn scraping or company website scraping |
| `decision_maker_title` | **NOT AVAILABLE** | Would need LinkedIn scraping or company website scraping |
| `company_linkedin_url` | **NOT AVAILABLE** | Would need web search or LinkedIn API |
| `personal_linkedin_url` | **NOT AVAILABLE** | Would need LinkedIn scraping |
| `email` | **NOT AVAILABLE** | Would need web scraping from company website |

### 🔄 Fields That Need Transformation

| Our Field | Source | Transformation Needed |
|-----------|--------|----------------------|
| `location_city` | `address` | Parse address string to extract city |
| `location_country` | Search parameter | Extract from original search location |
| `website_url` | `links.website` or `links.directions` | Use website if available, otherwise extract domain from directions |

## Current Code Issues

### Problem: Incorrect Field Access

The current code in `discovery/lead_discovery.py` tries to access fields that don't exist:

```python
# ❌ WRONG - These fields don't exist in SerpAPI response
result.get("website")           # Should be: result.get("links", {}).get("website")
result.get("phone")             # Should be: result.get("links", {}).get("phone")
result.get("employees")         # NOT AVAILABLE in SerpAPI
result.get("owner_name")        # NOT AVAILABLE in SerpAPI
result.get("email")             # NOT AVAILABLE in SerpAPI
```

### Solution: Correct Field Access

```python
# ✅ CORRECT - Access fields that actually exist
result.get("title")                              # Company name
result.get("links", {}).get("website")           # Website URL (optional)
result.get("links", {}).get("phone")             # Phone number (optional)
result.get("type")                               # Industry/business type
result.get("description")                        # Business description (optional)
result.get("address")                            # Full address string
result.get("rating")                             # Rating (for quality filtering)
result.get("reviews")                            # Review count (for quality filtering)
```

## Recommendations for Missing Fields

Since SerpAPI doesn't provide employee count, decision maker info, LinkedIn URLs, or emails, we have several options:

### Option 1: Mark as Unavailable (Quick Fix)
- Set these fields to `None` or `"N/A"`
- Focus on fields that ARE available
- Document limitations clearly

### Option 2: Add Secondary Data Sources (Better Quality)
- Use Google Places API for additional business details
- Scrape company websites for email addresses
- Use LinkedIn API or scraping for decision maker info
- Use company size estimation based on reviews/rating

### Option 3: Hybrid Approach (Recommended)
1. Extract all available data from SerpAPI
2. For high-quality leads (high rating, many reviews), attempt web scraping for missing fields
3. Mark fields as "N/A" only when truly unavailable after all attempts

## Implementation Priority

1. **Phase 1** (Immediate): Fix field extraction to use correct SerpAPI fields
2. **Phase 2** (Next): Add address parsing for city/country extraction
3. **Phase 3** (Future): Add secondary data sources for missing fields

## Example Correct Extraction

```python
def _parse_business_result(self, result: Dict) -> Optional[RawLead]:
    """Parse a single business result from SerpAPI."""
    
    # Extract available fields correctly
    company_name = result.get("title")
    if not company_name:
        return None
    
    # Extract links (nested object)
    links = result.get("links", {})
    website_url = links.get("website")
    phone = links.get("phone")
    
    # Extract other available fields
    industry = result.get("type")
    description = result.get("description")
    address = result.get("address", "")
    
    # Parse location from address
    location_city, location_country = self._parse_address(address)
    
    # Fields not available in SerpAPI - set to None
    employee_count = None
    decision_maker_name = None
    decision_maker_title = None
    company_linkedin_url = None
    personal_linkedin_url = None
    email = None
    
    return RawLead(
        company_name=company_name,
        website_url=website_url,
        location_city=location_city,
        location_country=location_country,
        industry=industry,
        employee_count=employee_count,
        description=description,
        decision_maker_name=decision_maker_name,
        decision_maker_title=decision_maker_title,
        company_linkedin_url=company_linkedin_url,
        personal_linkedin_url=personal_linkedin_url,
        email=email,
        phone=phone,
        source_data=result
    )
```

## Testing Notes

- Use the `scripts/test_serpapi_response.py` script to capture real API responses
- Saved responses are in `tests/fixtures/serpapi_responses/`
- Always test with real API responses, not mock data
- Verify field availability varies by business type and location
