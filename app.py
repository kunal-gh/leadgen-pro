from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import os
import glob
from demo_generator import generate_leads_dynamic
import time

app = Flask(__name__)

# MLOps: Global Telemetry State (Simulating Redis/Feature Store for demo)
global_telemetry = {
    "model_version": "v2.5.1-xgboost-champion",
    "challenger_version": "v3.0.0-lgbm-shadow",
    "inference_latency_ms": 0.0,
    "drift_status": "Calculating...",
    "features_processed": 0,
    "total_invocations": 0
}

def get_latest_leads_file():
    files = glob.glob("Verified_Leads_*.xlsx")
    # also check old files so dashboard doesn't break
    if not files:
        files = glob.glob("Verified_Indian_Leads_*.xlsx")
    if not files:
        return None
    return max(files, key=os.path.getctime)

@app.route('/')
def dashboard():
    latest_file = get_latest_leads_file()
    stats = {
        'total_leads': 0,
        'industries': 0,
        'cities': 0,
        'latest_file': latest_file or "None"
    }
    
    leads_data = []
    
    if latest_file:
        try:
            df = pd.read_excel(latest_file)
            stats['total_leads'] = len(df)
            stats['industries'] = df['Industry'].nunique() if 'Industry' in df.columns else 0
            stats['cities'] = df['Location'].nunique() if 'Location' in df.columns else 0
            
            # Get first 50 leads for display to keep UI fast
            leads_data = df.head(50).fillna("").to_dict('records')
        except Exception as e:
            print(f"Error reading Excel: {e}")
            
    return render_template('index.html', stats=stats, leads=leads_data, telemetry=global_telemetry)

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        
        # Parse inputs from the UI Modal
        raw_count = str(data.get('count', '50'))
        count = int(raw_count) if raw_count.isdigit() else 50
        
        raw_industries = data.get('industries', 'Digital Marketing, SaaS, Real Estate')
        industries = [i.strip() for i in raw_industries.split(',') if i.strip()]
        if not industries:
            industries = ['Digital Marketing Agency', 'SaaS Startup', 'Real Estate Brokerage']
            
        raw_locations = data.get('locations', 'Mumbai, Bangalore, Delhi')
        locations = [l.strip() for l in raw_locations.split(',') if l.strip()]
        if not locations:
            locations = ['Mumbai, Maharashtra', 'Bangalore, Karnataka', 'Delhi NCR']
            
        raw_sizes = data.get('sizes', '5-50, 50-200')
        sizes = [s.strip() for s in raw_sizes.split(',') if s.strip()]
        if not sizes:
            sizes = ['5-50 employees', '50-200 employees']
        
        # Call the dynamic generator logic
        df, output_filename, telemetry = generate_leads_dynamic(
            num_leads=count,
            industries=industries,
            locations=locations,
            sizes=sizes
        )
        
        # Update Global Telemetry State
        global global_telemetry
        global_telemetry["inference_latency_ms"] = telemetry["inference_latency_ms"]
        global_telemetry["drift_status"] = telemetry["drift_status"]
        global_telemetry["features_processed"] += telemetry["features_processed"]
        global_telemetry["total_invocations"] += 1
        
        return jsonify({
            'status': 'success',
            'message': f'Successfully generated {len(df)} leads strictly matching your filters.',
            'file': output_filename,
            'count': len(df),
            'telemetry': telemetry
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/download')
def download():
    latest_file = get_latest_leads_file()
    if latest_file:
        return send_file(latest_file, as_attachment=True)
    return "No leads generated yet", 404

@app.route('/api/mlops/metrics')
def mlops_metrics():
    """Prometheus-compatible endpoint for model health scraping"""
    metrics = [
        f"# HELP model_inference_latency_ms Average latency for XGBoost Champion",
        f"# TYPE model_inference_latency_ms gauge",
        f"model_inference_latency_ms {global_telemetry['inference_latency_ms']}",
        f"# HELP model_features_processed_total Total features processed by pipeline",
        f"# TYPE model_features_processed_total counter",
        f"model_features_processed_total {global_telemetry['features_processed']}",
        f"# HELP model_invocations_total Total algorithmic generations requested",
        f"# TYPE model_invocations_total counter",
        f"model_invocations_total {global_telemetry['total_invocations']}"
    ]
    return "\n".join(metrics), 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
