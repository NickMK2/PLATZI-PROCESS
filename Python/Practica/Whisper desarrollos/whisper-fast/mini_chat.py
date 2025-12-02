# mini_chat.py (con timeout y max_tokens configurables)
import os
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

LM_BASE_URL   = os.environ.get("LM_BASE_URL", "http://localhost:1234/v1")
LM_API_KEY    = os.environ.get("LM_API_KEY", "lm-studio")
DEFAULT_MODEL = os.environ.get("LM_MODEL", "qwen/qwen3-coder-30b")

# NUEVO: controla cuánto esperamos la respuesta de LM Studio
# (connect timeout, read timeout)
LM_TIMEOUT = int(os.environ.get("LM_TIMEOUT", "240"))
REQ_TIMEOUT = (10, LM_TIMEOUT)

# NUEVO: limita cuánto puede hablar el modelo en cada respuesta
LM_MAX_TOKENS = int(os.environ.get("LM_MAX_TOKENS", "400"))

HTML = r"""
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>HANNAH GESTIÓN PH S.A.S. — LM Studio Chat (LAN)</title>
<style>
  body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial;background:#0f172a;color:#e2e8f0;margin:0}
  header{padding:16px 20px;background:#111827;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
  .pill{padding:6px 10px;border-radius:999px;background:#1f2937;font-size:12px;opacity:.9}
  .ok{background:#064e3b;color:#a7f3d0}
  .bad{background:#7f1d1d;color:#fecaca}
  main{max-width:1000px;margin:24px auto;padding:0 16px}
  .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
  select,button{height:38px;border-radius:8px;border:1px solid #334155;background:#0b1220;color:#e2e8f0;padding:0 10px}
  button.primary{background:#1d4ed8;border-color:#1d4ed8}
  #chat{background:#0b1220;border:1px solid #1f2937;border-radius:12px;min-height:420px;padding:18px;margin-top:16px}
  .msg{margin:10px 0;padding:10px 12px;border-radius:10px;white-space:pre-wrap}
  .me{background:#1e293b}
  .bot{background:#111827}
  form{display:flex;gap:10px;margin-top:10px}
  textarea{flex:1;border-radius:10px;border:1px solid #334155;background:#0b1220;color:#e2e8f0;padding:10px;min-height:70px}
  .muted{opacity:.7}
</style>
</head>
<body>
<header>
  <div style="font-weight:700">HANNAH GESTIÓN PH S.A.S.</div>
  <div class="pill">LM Studio Chat (LAN)</div>
  <div id="apiTag" class="pill">API: {{api_base}}</div>
  <div id="srvTag" class="pill">Server: …</div>
</header>

<main>
  <div class="row">
    <label for="model">Modelo:</label>
    <select id="model"></select>
    <button id="reload" class="pill">Recargar</button>
    <span id="hint" class="muted"></span>
  </div>

  <div id="chat"></div>

  <form id="composer">
    <textarea id="text" placeholder="Escribe un mensaje y luego toca Enviar. En PC: Enter envía, Ctrl+Enter hace salto de línea…"></textarea>
    <button id="send" type="submit" class="primary">Enviar</button>
  </form>
</main>

<script>
const chat = document.getElementById('chat');
const text = document.getElementById('text');
const modelSel = document.getElementById('model');
const reloadBtn = document.getElementById('reload');
const srvTag = document.getElementById('srvTag');
const hint = document.getElementById('hint');

function line(role, content){
  const d = document.createElement('div');
  d.className = 'msg ' + (role==='user'?'me':'bot');
  d.textContent = content;
  chat.appendChild(d);
  chat.scrollTop = chat.scrollHeight;
}

async function ping(){
  srvTag.textContent = 'Server: comprobando…';
  try{
    const r = await fetch('/api/models');
    if(!r.ok) throw new Error('HTTP '+r.status);
    const data = await r.json();
    modelSel.innerHTML = '';
    (data||[]).forEach(id=>{
      const opt = document.createElement('option');
      opt.value = id; opt.textContent = id;
      modelSel.appendChild(opt);
    });
    srvTag.className = 'pill ok';
    srvTag.textContent = 'Servidor OK';
    hint.textContent = 'Usando ' + (modelSel.value || '(sin modelo)');
  }catch(e){
    srvTag.className = 'pill bad';
    srvTag.textContent = 'Servidor NO disponible';
  }
}
reloadBtn.onclick = ping;
ping();

document.getElementById('composer').addEventListener('submit', async (ev)=>{
  ev.preventDefault();
  const msg = text.value.trim();
  if(!msg) return;
  line('user', msg);
  text.value = '';

  const typing = document.createElement('div');
  typing.className='msg bot muted';
  typing.textContent='Escribiendo…';
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;

  try{
    const r = await fetch('/api/chat', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ model: modelSel.value, messages:[{role:'user', content: msg}] })
    });
    if(!r.ok) throw new Error('HTTP '+r.status);
    const data = await r.json();
    typing.remove();
    line('assistant', data.reply || '(sin respuesta)');
  }catch(e){
    typing.className='msg bot';
    typing.textContent='[Error] ' + e.message;
  }
});

// En PC: Enter envía; Ctrl+Enter inserta salto. En móvil usa el botón.
text.addEventListener('keydown', (ev)=>{
  if(ev.key==='Enter' && !ev.ctrlKey && !ev.shiftKey){
    if(!/Mobi|Android/i.test(navigator.userAgent)){ ev.preventDefault(); document.getElementById('send').click(); }
  }
});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, api_base=f"localhost:1234/v1")

@app.route("/api/models")
def api_models():
    try:
        r = requests.get(
            f"{LM_BASE_URL}/models",
            headers={"Authorization": f"Bearer {LM_API_KEY}"},
            timeout=REQ_TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        ids = [m["id"] for m in (data.get("data") or [])]
        if DEFAULT_MODEL not in ids:
            ids.append(DEFAULT_MODEL)
        return jsonify(ids)
    except Exception as e:
        print("[/api/models] ERROR:", e)
        return jsonify([]), 503

@app.route("/api/chat", methods=["POST"])
def api_chat():
    body = request.get_json(force=True) or {}
    messages = body.get("messages") or []
    model = body.get("model") or DEFAULT_MODEL

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.3,
        # NUEVO: limitar salida para evitar timeouts
        "max_tokens": LM_MAX_TOKENS,
    }
    headers = {
        "Authorization": f"Bearer {LM_API_KEY}",
        "Content-Type": "application/json",
    }

    print("[/api/chat] -->", {**payload, "messages": f"{len(messages)} msgs"})
    try:
        r = requests.post(
            f"{LM_BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
            timeout=REQ_TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        reply = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")
        print("[/api/chat] <-- ok")
        return jsonify({"reply": reply})
    except Exception as e:
        print("[/api/chat] ERROR:", repr(e))
        return jsonify({"error": str(e)}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8899)), debug=False)
