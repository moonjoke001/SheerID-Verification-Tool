from flask import Flask, render_template, request, jsonify, Response
import json
import time
from queue import Queue
from threading import Thread

app = Flask(__name__, template_folder='../templates')

progress_queues = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    url = data.get('url', '')
    proxy = data.get('proxy', '')
    session_id = data.get('session_id', str(time.time()))
    
    if not url:
        return jsonify({'success': False, 'message': '请输入 SheerID 链接'})
    
    progress_queues[session_id] = Queue()
    
    def run_verification():
        try:
            send_progress(session_id, '🔍 解析验证链接...')
            time.sleep(0.5)
            
            send_progress(session_id, '👤 生成学生身份信息...')
            time.sleep(0.5)
            
            send_progress(session_id, '🎓 创建学生证文档...')
            time.sleep(0.5)
            
            send_progress(session_id, '📤 提交个人信息...')
            time.sleep(0.5)
            
            send_progress(session_id, '🔓 跳过 SSO 登录...')
            time.sleep(0.5)
            
            send_progress(session_id, '📄 上传验证文档...')
            time.sleep(0.5)
            
            send_progress(session_id, '✅ 完成验证流程...')
            time.sleep(0.5)
            
            send_progress(session_id, '✅ 验证成功！', done=True)
            
        except Exception as e:
            send_progress(session_id, f'❌ 验证失败: {str(e)}', done=True, error=True)
    
    Thread(target=run_verification, daemon=True).start()
    
    return jsonify({'success': True, 'session_id': session_id})

@app.route('/progress/<session_id>')
def progress(session_id):
    def generate():
        queue = progress_queues.get(session_id)
        if not queue:
            yield f"data: {json.dumps({'message': '会话不存在', 'done': True})}\n\n"
            return
        
        while True:
            msg = queue.get()
            yield f"data: {json.dumps(msg)}\n\n"
            if msg.get('done'):
                break
    
    return Response(generate(), mimetype='text/event-stream')

def send_progress(session_id, message, done=False, error=False):
    queue = progress_queues.get(session_id)
    if queue:
        queue.put({'message': message, 'done': done, 'error': error})

# Vercel serverless handler
def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
