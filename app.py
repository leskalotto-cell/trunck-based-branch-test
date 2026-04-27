from flask import Flask, jsonify, request

app = Flask(__name__)

# Simpel in-memory datastore
data_store = []

@app.route('/')
def home():
    """Velkomstside"""
    return jsonify({
        'message': 'Velkommen til Flask API',
        'version': '1.0.0'
    })

@app.route('/api/hello')
def hello():
    """Returnerer en simpel hilsen"""
    return jsonify({
        'message': 'Hej fra API\'en!',
        'status': 'success'
    })

@app.route('/api/hello/<name>')
def hello_name(name):
    """Returnerer en personaliseret hilsen"""
    return jsonify({
        'message': f'Hej {name}!',
        'name': name,
        'status': 'success'
    })

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    """Håndterer GET og POST requests for data"""
    if request.method == 'POST':
        # Modtag JSON data
        json_data = request.get_json()
        
        if json_data is None:
            return jsonify({
                'error': 'Ingen JSON data modtaget',
                'status': 'error'
            }), 400
        
        # Tilføj data til store
        data_store.append(json_data)
        
        return jsonify({
            'message': 'Data gemt',
            'data': json_data,
            'id': len(data_store) - 1,
            'status': 'success'
        }), 201
    
    else:  # GET
        return jsonify({
            'message': 'Alle gemte data',
            'count': len(data_store),
            'data': data_store,
            'status': 'success'
        })

@app.route('/api/data/<int:data_id>', methods=['GET', 'DELETE'])
def get_data_by_id(data_id):
    """Få eller slet specifik data by ID"""
    if data_id < 0 or data_id >= len(data_store):
        return jsonify({
            'error': 'Data ikke fundet',
            'status': 'error'
        }), 404
    
    if request.method == 'DELETE':
        deleted = data_store.pop(data_id)
        return jsonify({
            'message': 'Data slettet',
            'deleted_data': deleted,
            'status': 'success'
        })
    
    else:  # GET
        return jsonify({
            'id': data_id,
            'data': data_store[data_id],
            'status': 'success'
        })

@app.route('/api/status')
def status():
    """API status endpoint"""
    return jsonify({
        'status': 'running',
        'total_items': len(data_store),
        'message': 'API fungerer normalt'
    })

@app.errorhandler(404)
def not_found(error):
    """Håndter 404 fejl"""
    return jsonify({
        'error': 'Endpoint ikke fundet',
        'status': 'error'
    }), 404

if __name__ == '__main__':
    # Start Flask serveren
    app.run(
        host='127.0.0.1',  # Lytter på localhost
        port=5000,
        debug=True  # Debug mode - deaktivér i produktion
    )
print("🚀 Flask API starter på http://127.0.0.1:5000")

print (hello world123)
