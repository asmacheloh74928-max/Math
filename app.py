import streamlit as st

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="ห้องเรียนตรรกศาสตร์คณิตศาสตร์ - Logic Lab",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ตกแต่งสไตล์ Retro Pastel แบบภาพตัวอย่าง
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Kanit', sans-serif;
    }
    
    .stApp {
        background-color: #FFF0F3;
    }

    /* ตกแต่ง Sidebar ด้านข้าง */
    [data-testid="stSidebar"] {
        background-color: #FFE5EC;
        border-right: 3px solid #2B2B2B;
    }

    /* การ์ดหัวเรื่องหลัก */
    .title-card {
        background-color: #FFFFFF;
        border: 3px solid #2B2B2B;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 4px 4px 0px #2B2B2B;
        margin-bottom: 20px;
    }

    /* การ์ดเนื้อหา */
    .content-card {
        background-color: #FFFFFF;
        border: 3px solid #2B2B2B;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 5px 5px 0px #2B2B2B;
        margin-bottom: 15px;
    }

    /* ป้ายย่อย */
    .badge {
        background-color: #FFD6A5;
        border: 2px solid #2B2B2B;
        border-radius: 8px;
        padding: 4px 12px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
        color: #2B2B2B;
    }

    /* กล่องสูตรเน้นพิเศษ */
    .formula-box {
        background-color: #CAFFBF;
        border: 2.5px solid #2B2B2B;
        border-radius: 12px;
        padding: 15px;
        font-size: 1.1rem;
        font-weight: bold;
        color: #2B2B2B;
        box-shadow: 3px 3px 0px #2B2B2B;
        margin: 10px 0px;
    }

    .success-box {
        background-color: #E2F0CB;
        border: 2px solid #2B2B2B;
        border-radius: 10px;
        padding: 10px 15px;
        color: #2B2B2B;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR: เมนูด้านข้างแบบละเอียด
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🧠 Logic Learning Hub")
    st.markdown("---")
    
    menu = st.radio(
        "📌 เลือกหัวข้อบทเรียน:",
        [
            "🏠 00. หน้าหลัก & ภาพรวม",
            "📖 01. ประพจน์ (Proposition)",
            "🔗 02. ตัวเชื่อมประพจน์ และ (∧)",
            "🔗 03. ตัวเชื่อมประพจน์ หรือ (∨)",
            "🔗 04. ตัวเชื่อม ถ้า...แล้ว (→)",
            "🔗 05. ตัวเชื่อม ก็ต่อเมื่อ (↔)",
            "🚫 06. นิเสธของประพจน์ (~)",
            "📊 07. ตารางความจริง (Truth Table)",
            "🔄 08. รูปแบบประพจน์ที่สมพากย์กัน",
            "✨ 09. สัจนิรันดร์ (Tautology)",
            "⚖️ 10. การอ้างเหตุผล (Arguments)",
            "🔍 11. ตัวบ่งปริมาณ (Quantifiers)",
            "🎯 12. คลังข้อสอบวัดความเข้าใจ"
        ]
    )
    
    st.markdown("---")
    st.caption("จัดทำโดย: นางสาวอัสมะ เจะเลาะ")

# ---------------------------------------------------------
# DISPLAY CONTENT: แสดงเนื้อหาตามเมนูที่เลือก (1 หน้าเต็มๆ)
# ---------------------------------------------------------

if "00. หน้าหลัก" in menu:
    st.markdown("""
    <div class="title-card">
        <h2 style="margin:0; color:#2B2B2B;">🏠 Welcome to Calculus & Logic Sandbox</h2>
        <p style="color:#555; margin-top:5px;">เว็บแอปพลิเคชันเพื่อการเรียนรู้ตรรกศาสตร์คณิตศาสตร์ สรุปสูตรครบถ้วน แม่นยำ และอินเทอร์แอกทีฟ</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="content-card">
            <div class="badge">💡 คำแนะนำการใช้งาน</div>
            <p>เลือกหัวข้อบทเรียนย่อยจาก <b>Sidebar เมนูด้านข้าง</b> เพื่อเข้าสู่บทเรียนแต่ละเรื่องได้ทันทีครับ</p>
            <ul>
                <li>สรุปเนื้อหาและนิยามสั้น กระชับ</li>
                <li>แสดงสูตรสำคัญและตารางความจริงชัดเจน</li>
                <li>มีแบบฝึกหัดโต้ตอบในทุกหัวข้อ</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="content-card">
            <div class="badge">🎯 จุดประสงค์การเรียนรู้</div>
            <p>1. เข้าใจความหมายของประพจน์และค่าความจริง</p>
            <p>2. สามารถใช้ตัวเชื่อมตรรกศาสตร์และสร้างตารางความจริงได้</p>
            <p>3. ตรวจสอบสัจนิรันดร์และการอ้างเหตุผลได้อย่างถูกต้อง</p>
        </div>
        """, unsafe_allow_html=True)

elif "01. ประพจน์" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">01. ประพจน์ (Proposition)</div>
        <h3>📌 นิยามของประพจน์</h3>
        <p><b>ประพจน์</b> คือ ประโยคบอกเล่าหรือประโยคปฏิเสธ ที่มีค่าความจริงเป็น <b>"จริง (T)"</b> หรือ <b>"เท็จ (F)"</b> อย่างใดอย่างหนึ่งเพียงอย่างเดียวเท่านั้น</p>
        <hr>
        <h4>❌ ประโยคที่ไม่เป็นประพจน์:</h4>
        <p>คำถาม, คำสั่ง, ขอร้อง, อ้อนวอน, อุทาน, ประโยคคำสั่ง เช่น "กรุณาอย่าเดินลัดสนาม", "ทำไมวันนี้ฝนตก?"</p>
    </div>
    """, unsafe_allow_html=True)
    
    # แบบฝึกหัดโต้ตอบประจำหน้า
    st.subheader("✍️ ตรวจสอบความเข้าใจ")
    ans = st.radio("ข้อใดเป็นประพจน์?", ["ก) ช่วยปิดประตูให้หน่อย", "ข) จังหวัดเชียงใหม่ อยู่ภาคใต้ของไทย", "ค) อุ๊ย! ตกใจหมดเลย"], index=None)
    if ans == "ข) จังหวัดเชียงใหม่ อยู่ภาคใต้ของไทย":
        st.balloons()
        st.markdown('<div class="success-box">🎉 ถูกต้องครับ! เป็นประพจน์ที่มีค่าความจริงเป็น "เท็จ (F)"</div>', unsafe_allow_html=True)

elif "02. ตัวเชื่อมประพจน์ และ" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">02. ตัวเชื่อม "และ" (AND : ∧)</div>
        <h3>📌 กฎของตัวเชื่อม "และ" (∧)</h3>
        <p>ประพจน์ $p \land q$ จะมีค่าความจริงเป็น <b>"จริง (T)"</b> ก็ต่อเมื่อ <b>ทั้งสองประพจน์เป็นจริงทั้งคู่เท่านั้น</b></p>
        <div class="formula-box">T ∧ T = T (กรณีอื่นๆ เป็น F ทั้งหมด)</div>
    </div>
    """, unsafe_allow_html=True)

elif "03. ตัวเชื่อมประพจน์ หรือ" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">03. ตัวเชื่อม "หรือ" (OR : ∨)</div>
        <h3>📌 กฎของตัวเชื่อม "หรือ" (∨)</h3>
        <p>ประพจน์ $p \lor q$ จะมีค่าความจริงเป็น <b>"เท็จ (F)"</b> ก็ต่อเมื่อ <b>ทั้งสองประพจน์เป็นเท็จทั้งคู่เท่านั้น</b></p>
        <div class="formula-box">F ∨ F = F (กรณีอื่นๆ เป็น T ทั้งหมด)</div>
    </div>
    """, unsafe_allow_html=True)

elif "04. ตัวเชื่อม ถ้า...แล้ว" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">04. ตัวเชื่อม "ถ้า...แล้ว" (Implication : →)</div>
        <h3>📌 กฎของตัวเชื่อม "ถ้า...แล้ว" (→)</h3>
        <p>ประพจน์ $p \rightarrow q$ จะมีค่าความจริงเป็น <b>"เท็จ (F)"</b> ก็ต่อเมื่อ <b>หน้าจริง หลังเท็จ เท่านั้น</b></p>
        <div class="formula-box">T → F = F (กรณีอื่นๆ เป็น T ทั้งหมด)</div>
    </div>
    """, unsafe_allow_html=True)

elif "05. ตัวเชื่อม ก็ต่อเมื่อ" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">05. ตัวเชื่อม "ก็ต่อเมื่อ" (Equivalence : ↔)</div>
        <h3>📌 กฎของตัวเชื่อม "ก็ต่อเมื่อ" (↔)</h3>
        <p>ประพจน์ $p \leftrightarrow q$ จะเป็น <b>"จริง (T)"</b> เมื่อทั้งสองประพจน์มี<b>ค่าความจริงเหมือนกัน</b></p>
        <div class="formula-box">T ↔ T = T , F ↔ F = T</div>
    </div>
    """, unsafe_allow_html=True)

elif "06. นิเสธของประพจน์" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">06. นิเสธ (NOT : ~)</div>
        <h3>📌 นิเสธของประพจน์ (~p)</h3>
        <p>คือการตรงกันข้ามของค่าความจริงเดิม</p>
        <ul>
            <li>ถ้า $p$ เป็น T จะได้ $\sim p$ เป็น <b>F</b></li>
            <li>ถ้า $p$ เป็น F จะได้ $\sim p$ เป็น <b>T</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif "08. รูปแบบประพจน์ที่สมพากย์กัน" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">08. สูตรสมพากย์ที่ออกสอบบ่อย (Equivalences)</div>
        <ul>
            <li><b>กฎการเปลี่ยนถ้า...แล้ว:</b> $p \rightarrow q \equiv \sim p \lor q$</li>
            <li><b>กฎ De Morgan:</b> $\sim(p \land q) \equiv \sim p \lor \sim q$</li>
            <li><b>กฎ De Morgan:</b> $\sim(p \lor q) \equiv \sim p \land \sim q$</li>
            <li><b>กฎผลต่างนิเสธ:</b> $p \rightarrow q \equiv \sim q \rightarrow \sim p$</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif "09. สัจนิรันดร์" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">09. สัจนิรันดร์ (Tautology)</div>
        <h3>📌 นิยามสัจนิรันดร์</h3>
        <p>คือรูปแบบของประพจน์ที่มีค่าความจริงเป็น <b>"จริง (T) ในทุกกรณี"</b> ไม่ว่าประพจน์ย่อยจะมีค่าความจริงเป็นอย่างไรก็ตาม</p>
        <p><b>วิธีตรวจสอบ:</b> สมมติให้เป็นเท็จ (F) แล้วหาข้อขัดแย้ง</p>
    </div>
    """, unsafe_allow_html=True)

elif "12. คลังข้อสอบ" in menu:
    st.markdown("""
    <div class="content-card">
        <div class="badge">12. แบบทดสอบประเมินผล</div>
        <h3>🎯 ทดสอบความรู้เรื่องตรรกศาสตร์</h3>
    </div>
    """, unsafe_allow_html=True)
    
    q1 = st.radio("ข้อ 1: ประพจน์ $T \rightarrow F$ มีค่าความจริงเป็นอะไร?", ["จริง (T)", "เท็จ (F)"], index=None)
    if q1 == "เท็จ (F)":
        st.success("ถูกต้องครับ!")

else:
    st.markdown("""
    <div class="content-card">
        <div class="badge">บทเรียนกำลังเตรียมข้อมูล</div>
        <p>สามารถเลือกหัวข้ออื่นใน Sidebar เพื่อเรียนรู้ได้ทันทีครับ</p>
    </div>
    """, unsafe_allow_html=True)
