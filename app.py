import os
import sys
from flask import Flask, render_template, request, jsonify

# Add current dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from algorithms.cpu_scheduler import (
    schedule_fcfs, schedule_sjf, schedule_srtf,
    schedule_round_robin, schedule_priority
)
from algorithms.banker import check_safety, request_resources, calculate_need
from algorithms.page_replacement import simulate_fifo, simulate_lru, simulate_optimal
from algorithms.disk_scheduler import schedule_disk
from algorithms.quiz_data import QUIZ_QUESTIONS, CHEATSHEET_TOPICS

app = Flask(__name__)

# Student & Project Metadata
PROJECT_META = {
    "student_name": "Jeevika S",
    "project_number": 13,
    "project_title": "Operating Systems Concepts Explainer Pack",
    "course": "Operating Systems & Systems Programming",
    "version": "1.0.0",
    "stack": ["Python 3.12", "Flask", "HTML5", "CSS3", "JavaScript (ES6+)", "Bootstrap 5"]
}

@app.route('/')
def home():
    return render_template('index.html', meta=PROJECT_META)


@app.route('/api/project-info', methods=['GET'])
def get_project_info():
    return jsonify(PROJECT_META)


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Jeevika S - Operating Systems Concepts Explainer Pack",
        "author": "Jeevika S",
        "topic": "#13"
    })


@app.route('/api/cpu-scheduling', methods=['POST'])
def api_cpu_scheduling():
    try:
        data = request.get_json(force=True)
        algorithm = data.get('algorithm', 'FCFS').upper()
        processes = data.get('processes', [])
        quantum = int(data.get('quantum', 2))

        if not processes:
            return jsonify({'error': 'Processes list cannot be empty'}), 400

        # Validate process format
        clean_procs = []
        for p in processes:
            clean_procs.append({
                'id': str(p.get('id', '')),
                'at': int(p.get('at', 0)),
                'bt': int(p.get('bt', 1)),
                'priority': int(p.get('priority', 1))
            })

        if algorithm == 'FCFS':
            result = schedule_fcfs(clean_procs)
        elif algorithm == 'SJF':
            result = schedule_sjf(clean_procs)
        elif algorithm == 'SRTF':
            result = schedule_srtf(clean_procs)
        elif algorithm == 'RR':
            result = schedule_round_robin(clean_procs, quantum)
        elif algorithm == 'PRIORITY':
            result = schedule_priority(clean_procs, preemptive=False)
        elif algorithm == 'PRIORITY_PREEMPTIVE':
            result = schedule_priority(clean_procs, preemptive=True)
        else:
            return jsonify({'error': f'Unsupported algorithm: {algorithm}'}), 400

        result['algorithm'] = algorithm
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/bankers-algorithm', methods=['POST'])
def api_banker():
    try:
        data = request.get_json(force=True)
        available = [int(x) for x in data.get('available', [])]
        max_matrix = [[int(x) for x in row] for row in data.get('max_matrix', [])]
        alloc_matrix = [[int(x) for x in row] for row in data.get('alloc_matrix', [])]

        if not available or not max_matrix or not alloc_matrix:
            return jsonify({'error': 'Available vector, Max matrix, and Allocation matrix are required'}), 400

        result = check_safety(available, max_matrix, alloc_matrix)
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/bankers-request', methods=['POST'])
def api_banker_request():
    try:
        data = request.get_json(force=True)
        available = [int(x) for x in data.get('available', [])]
        max_matrix = [[int(x) for x in row] for row in data.get('max_matrix', [])]
        alloc_matrix = [[int(x) for x in row] for row in data.get('alloc_matrix', [])]
        req_pid = int(data.get('pid', 0))
        req_vector = [int(x) for x in data.get('request', [])]

        result = request_resources(available, max_matrix, alloc_matrix, req_pid, req_vector)
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/page-replacement', methods=['POST'])
def api_page_replacement():
    try:
        data = request.get_json(force=True)
        algorithm = data.get('algorithm', 'FIFO').upper()
        raw_pages = data.get('pages', [])
        num_frames = int(data.get('num_frames', 3))

        if isinstance(raw_pages, str):
            pages = [int(x.strip()) for x in raw_pages.replace(',', ' ').split() if x.strip()]
        else:
            pages = [int(x) for x in raw_pages]

        if not pages:
            return jsonify({'error': 'Page reference string cannot be empty'}), 400

        if num_frames < 1:
            return jsonify({'error': 'Number of frames must be at least 1'}), 400

        if algorithm == 'FIFO':
            result = simulate_fifo(pages, num_frames)
        elif algorithm == 'LRU':
            result = simulate_lru(pages, num_frames)
        elif algorithm in ['OPTIMAL', 'OPT']:
            result = simulate_optimal(pages, num_frames)
        else:
            return jsonify({'error': f'Unsupported algorithm: {algorithm}'}), 400

        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/disk-scheduling', methods=['POST'])
def api_disk_scheduling():
    try:
        data = request.get_json(force=True)
        algorithm = data.get('algorithm', 'SCAN').upper()
        raw_requests = data.get('requests', [])
        initial_head = int(data.get('initial_head', 50))
        disk_size = int(data.get('disk_size', 200))
        direction = data.get('direction', 'right').lower()

        if isinstance(raw_requests, str):
            requests = [int(x.strip()) for x in raw_requests.replace(',', ' ').split() if x.strip()]
        else:
            requests = [int(x) for x in raw_requests]

        if not requests:
            return jsonify({'error': 'Disk requests cannot be empty'}), 400

        result = schedule_disk(algorithm, requests, initial_head, disk_size, direction)
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/quiz', methods=['GET'])
def api_quiz():
    return jsonify({'success': True, 'questions': QUIZ_QUESTIONS})


@app.route('/api/cheatsheet', methods=['GET'])
def api_cheatsheet():
    return jsonify({'success': True, 'topics': CHEATSHEET_TOPICS})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"================================================================")
    print(f"  OPERATING SYSTEMS CONCEPTS EXPLAINER PACK (Topic #13)")
    print(f"  Student: Jeevika S")
    print(f"  Server running on http://127.0.0.1:{port}")
    print(f"================================================================")
    app.run(host='0.0.0.0', port=port, debug=False)
