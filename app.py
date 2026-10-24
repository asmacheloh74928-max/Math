import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Logic Learning Sandbox - ตรรกศาสตร์เชิงคณิตศาสตร์",
    page_icon="🧮",
    layout="wide",
)

# ตกแต่ง CSS เพิ่มเติมให้หน้าเว็บดูสวยงามและน่าเรียนยิ่งขึ้น
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 20px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4f46e5;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- ส่วนหัวของเว็บแอป (Header Dashboard) ---
st.markdown(
    '<p class="main-header">🧮 Logic Learning Sandbox</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-header">สื่อการเรียนรู้อิเล็กทรอนิกส์เชิงโต้ตอบ วิชาตรรกศาสตร์เชิงคณิตศาสตร์ | คณะครุศาสตร์ สาขาคณิตศาสตร์</p>',
    unsafe_allow_html=True,
)

# --- สร้างระบบเมนูแบบแถบด้านบน (Top Tabs) ทันสมัย ไม่ซ้ำใคร ---
tabs = st.tabs([
    "🏠 หน้าแรก",
    "📖 บทที่ 1: ประพจน์",
    "🔗 บทที่ 2: ตัวเชื่อม",
    "✨ บทที่ 3: สัจนิรันดร์",
    "⚖️ บทที่ 4: การอ้างเหตุผล",
    "🔍 บทที่ 5: ตัวบ่งปริมาณ",
    "📈 บทที่ 6: การพิสูจน์",
    "📋 สรุปสูตรด่วน",
])

# ==================== TAB 1: หน้าแรก ====================
with tabs[0]:
    st.markdown("### 👋 ยินดีต้อนรับสู่ห้องเรียนตรรกศาสตร์ดิจิทัล")
    st.write(
        "เว็บแอปพลิเคชันนี้จัดทำขึ้นเพื่อช่วยให้การเรียนรู้เรื่อง **ตรรกศาสตร์เชิงคณิตศาสตร์ (Mathematical Logic)** เป็นเรื่องง่าย สนุก และสามารถทดสอบความเข้าใจได้ทันทีผ่านระบบอินเตอร์แอคทีฟ"
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label="📚 บทเรียนทั้งหมด", value="6 บทหลัก", delta="ครอบคลุมเนื้อหา"
        )
    with col2:
        st.metric(
            label="💡 รูปแบบการเรียน",
            value="Interactive",
            delta="กดตอบ-รู้ผลทันที",
        )
    with col3:
        st.metric(
            label="📋 คลังสูตร", value="Cheat Sheet", delta="เปิดดูขณะทำโจทย์"
        )
    with col4:
        st.metric(label="🎯 กลุ่มเป้าหมาย", value="นักเรียน/นักศึกษา", delta="มัธยมปลายขึ้นไป")

    st.markdown("---")
    st.markdown("#### 🚀 คำแนะนำการใช้งาน")
    st.info(
        "1. เลือกหัวข้อบทเรียนจาก **แถบเมนูด้านบน** เพื่อศึกษาเนื้อหาและทำแบบฝึกหัด\n"
        "2. หากลืมสูตรหรือสมบัติสำคัญ สามารถคลิกที่แท็บ **'📋 สรุปสูตรด่วน'** ได้ตลอดเวลา\n"
        "3. ทุกข้อจะมีระบบตรวจคำตอบอัตโนมัติ พร้อมคำอธิบายวิธีทำอย่างละเอียด"
    )

    st.markdown("---")
    st.caption(
        "© จัดทำโดย: นางสาวอัสมะ เจะเลาะ และ นูรูลฮูดา เปาะแต | คณะครุศาสตร์ สาขาวิชาคณิตศาสตร์ มหาวิทยาลัยราชภัฏธนบุรี"
    )

# ==================== TAB 2: บทที่ 1 ====================
with tabs[1]:
    st.header("📖 บทที่ 1: บทนำ ประพจน์ และกฎการให้เหตุผลเบื้องต้น")
    st.markdown("---")

    st.markdown(
        """
    <div class="card">
    <h4>💡 แนวคิดหลัก (Core Concepts)</h4>
    <p><b>ประพจน์ (Proposition)</b> คือ ประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง (True: T) หรือเท็จ (False: F) อย่างใดอย่างหนึ่งเท่านั้น ประโยคคำถาม คำสั่ง หรืออุทาน จะไม่ถือว่าเป็นประพจน์</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("กฎการอ้างเหตุผลเบื้องต้น (Modus Ponens)")
    st.latex(r"p \rightarrow q, \quad p \quad \vdash \quad q")
    st.write(
        "หากเหตุการณ์ $p$ นำไปสู่ $q$ และเราทราบแน่ชัดว่า $p$ เป็นจริง เราจึงสามารถสรุปได้อย่างสมเหตุสมผลว่า $q$ เป็นจริง"
    )

    st.markdown("---")
    st.subheader("📝 แบบฝึกหัดทดสอบความเข้าใจ")
    q1 = st.radio(
        "ข้อที่ 1: ประโยคในข้อใดต่อไปนี้ 'เป็นประพจน์'",
        (
            "เลือกคำตอบ...",
            "ก. ห้ามส่งเสียงดังในห้องสมุด",
            "ข. 2 + 3 = 6",
            "ค. คุณกำลังทำอะไรอยู่?",
            "ง. Ouch! เจ็บจัง",
        ),
        key="b1_q1",
    )

    if q1 != "เลือกคำตอบ...":
        if "ข. 2 + 3 = 6" in q1:
            st.success(
                "🎉 ถูกต้องนะคร้าบ/ค่ะ! '2 + 3 = 6' เป็นประโยคบอกเล่าที่มีค่าความจริงเป็นเท็จ (F) จึงถือเป็นประพจน์"
            )
        else:
            st.error(
                "❌ ยังไม่ถูกต้องครับ/ค่ะ ประโยคคำสั่ง คำถาม และอุทาน ไม่ถือเป็นประพจน์ ลองใหม่อีกครั้งนะ!"
            )

# ==================== TAB 3: บทที่ 2 ====================
with tabs[2]:
    st.header("🔗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง")
    st.markdown("---")

    st.markdown(
        """
    <div class="card">
    <h4>📌 สรุปตัวเชื่อมสำคัญ</h4>
    <ul>
        <li><b>นิเสธ ($\neg p$):</b> กลับค่าความจริงตรงกันข้าม</li>
        <li><b>และ ($p \wedge q$):</b> เป็นจริงเฉพาะกรณีที่เป็นจริงทั้งคู่</li>
        <li><b>หรือ ($p \vee q$):</b> เป็นเท็จเฉพาะกรณีที่เป็นเท็จทั้งคู่</li>
        <li><b>ถ้า...แล้ว ($p \rightarrow q$):</b> เป็นเท็จกรณีเดียวคือ จริง $\rightarrow$ เท็จ</li>
        <li><b>ก็ต่อเมื่อ ($p \leftrightarrow q$):</b> เป็นจริงเมื่อมีค่าความจริงเหมือนกัน</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("กฎสมมูลที่สำคัญ (Useful Identities)")
    st.latex(r"p \rightarrow q \equiv \neg p \vee q")
    st.latex(r"\neg(p \wedge q) \equiv \neg p \vee \neg q \quad (\text{กฎของเดอมอร์แกน})")

    st.markdown("---")
    st.subheader("📝 แบบฝึกหัดทดสอบความเข้าใจ")
    q2 = st.radio(
        "ข้อที่ 1: ประพจน์ $p \rightarrow q$ สมมูลกับข้อใดมากที่สุด?",
        (
            "เลือกคำตอบ...",
            "$\\neg p \\vee q$",
            "$p \\wedge \\neg q$",
            "$\\neg p \\wedge \\neg q$",
            "$q \\rightarrow p$",
        ),
        key="b2_q1",
    )

    if q2 != "เลือกคำตอบ...":
        if "$\\neg p \\vee q$" in q2:
            st.success(
                "🎉 ยอดเยี่ยม! สมบัตินี้เรียกว่าการเปลี่ยนรูปเครื่องหมายลูกศรเป็นเครื่องหมายหรือ (นิเสธหน้า หรือ หลัง)"
            )
        else:
            st.error(
                "❌ ยังผิดอยู่จ้า ลองเช็คสูตรในหน้าสรุปสูตรด่วนดูอีกรอบนะ!"
            )

# ==================== TAB 4: บทที่ 3 ====================
with tabs[3]:
    st.header("✨ บทที่ 3: สัจนิรันดร์ (Tautologies)")
    st.markdown("---")

    st.markdown(
        """
    <div class="card">
    <h4>🔍 สัจนิรันดร์คืออะไร?</h4>
    <p><b>สัจนิรันดร์ (Tautology)</b> คือ ประพจน์ที่มีค่าความจริงเป็น <b>จริง (T) ทุกกรณี</b> ในตารางค่าความจริง ไม่ว่าประพจน์ย่อยจะมีค่าความจริงเป็นอะไรก็ตาม</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("ตัวอย่างการตรวจสอบสัจนิรันดร์")
    st.write("ต้องการตรวจสอบว่า $(p \wedge q) \rightarrow p$ เป็นสัจนิรันดร์หรือไม่?")
    with st.expander("👉 คลิกเพื่อดูวิธีทำและเฉลี่ยอย่างละเอียด"):
        st.write(
            "1. สมมติให้ประพจน์หลักมีค่าเป็นเท็จ ($F$) ในกรณีที่เป็นเครื่องหมาย $\\rightarrow$\n"
            "2. จะเกิดขึ้นได้กรณีเดียวคือ เหตุเป็นจริง ($T$) และผลเป็นเท็จ ($F$)\n"
            "3. กำหนดให้ $p = F$ แต่จะทำให้เหตุส่วนหน้าขัดแย้งกันเอง\n"
            "4. **สรุป:** ไม่สามารถทำให้เป็นเท็จได้ ดังนั้นประพจน์นี้จึงเป็น **สัจนิรันดร์**"
        )

    st.markdown("---")
    st.subheader("📝 แบบฝึกหัดทดสอบความเข้าใจ")
    q3 = st.radio(
        "ข้อที่ 1: ประพจน์ $p \vee \neg p$ มีลักษณะเป็นอย่างไร?",
        (
            "เลือกคำตอบ...",
            "เป็นสัจนิรันดร์ (Tautology)",
            "เป็นข้อขัดแย้ง (Contradiction)",
            "เป็นประพจน์สมมูล",
        ),
        key="b3_q1",
    )
    if q3 != "เลือกคำตอบ...":
        if "สัจนิรันดร์" in q3:
            st.success(
                "🎉 ถูกต้องครับ! ไม่ว่า $p$ จะเป็นจริงหรือเท็จ ผลลัพธ์ของ $p \\vee \\neg p$ จะเป็นจริงเสมอ"
            )
        else:
            st.error("❌ ยังไม่ถูกต้อง ลองแทนค่า $p=T$ หรือ $p=F$ ดูนะ")

# ==================== TAB 5: บทที่ 4 ====================
with tabs[4]:
    st.header("⚖️ บทที่ 4: การอ้างเหตุผล (Arguments)")
    st.markdown("---")

    st.write(
        "การอ้างเหตุผลประกอบด้วย **เหตุ ($P_1, P_2, ..., P_n$)** และ **ผล ($C$)** การอ้างเหตุผลจะ **สมเหตุสมผล (Valid)** ก็ต่อเมื่อในกรณีที่เหตุทุกข้อเป็นจริงทั้งหมด ผลลัพธ์ต้องเป็นจริงตามด้วยเสมอ"
    )

    st.markdown("---")
    st.subheader("📝 แบบฝึกหัดทดสอบความเข้าใจ")
    q4 = st.radio(
        "ข้อที่ 1: รูปแบบการอ้างเหตุผล $p \\rightarrow q, \\neg q \\vdash \\neg p$ มีชื่อเรียกว่าอะไร?",
        (
            "เลือกคำตอบ...",
            "Modus Ponens",
            "Modus Tollens",
            "Hypothetical Syllogism",
        ),
        key="b4_q1",
    )
    if q4 != "เลือกคำตอบ...":
        if "Modus Tollens" in q4:
            st.success(
                "🎉 ถูกต้อง! Modus Tollens คือกฎการปฏิเสธผลเพื่อย้อนกลับไปปฏิเสธเหตุ"
            )
        else:
            st.error("❌ ผิดครับ คำตอบที่ถูกต้องคือ Modus Tollens")

# ==================== TAB 6: บทที่ 5 ====================
with tabs[5]:
    st.header("🔍 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)")
    st.markdown("---")

    st.markdown(
        """
    <div class="card">
    <h4>📌 ตัวบ่งปริมาณ (Quantifiers)</h4>
    <ul>
        <li><b>สำหรับทุกคน ($\forall x P(x)$):</b> เป็นจริงเมื่อ $P(x)$ เป็นจริงสำหรับทุกสมาชิกในเอกภพสัมพัทธ์</li>
        <li><b>สำหรับบางตัว ($\exists x P(x)$):</b> เป็นจริงเมื่อมีสมาชิกอย่างน้อยหนึ่งตัวที่ทำให้ $P(x)$ เป็นจริง</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("กฎการเติมและกระจายนิเสธตัวบ่งปริมาณ")
    st.latex(r"\neg \forall x P(x) \equiv \exists x \neg P(x)")
    st.latex(r"\neg \exists x P(x) \equiv \forall x \neg P(x)")

# ==================== TAB 7: บทที่ 6 ====================
with tabs[6]:
    st.header("📈 บทที่ 6: การอุปนัยและนิรนัย (Inductive & Deductive)")
    st.markdown("---")

    st.write(
        "**การอุปนัยเชิงคณิตศาสตร์ (Mathematical Induction)** เป็นวิธีการพิสูจน์ข้อความสำหรับจำนวนเต็มบวก $n$ ทุกตัว โดยประกอบด้วย 2 ขั้นตอนสำคัญ:"
    )
    st.markdown(
        """
    1. **Base Case:** แสดงว่าข้อความจริงเมื่อ $n = 1$
    2. **Inductive Step:** สมมติว่าจริงเมื่อ $n = k$ แล้วพิสูจน์ให้ได้ว่าต้องจริงสำหรับ $n = k + 1$ ด้วย
    """
    )

# ==================== TAB 8: หน้าสรุปสูตรด่วน (Cheat Sheet) ====================
with tabs[7]:
    st.header("📋 หน้าสรุปสูตรและสมบัติสำคัญ (Cheat Sheet)")
    st.subheader(
        "💡 หน้ารวมสูตรฉบับพกพา สำหรับเปิดดูทบทวนด่วนขณะกำลังทำโจทย์ฝึกหัด"
    )
    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### 🔗 สมบัติและการสมมูลที่สำคัญ")
        st.success(
            """
        * $p \\rightarrow q \\equiv \\neg p \\vee q$
        * $\\neg(p \\wedge q) \\equiv \\neg p \\vee \\neg q$
        * $\\neg(p \\vee q) \\equiv \\neg p \\wedge \\neg q$
        * $p \\leftrightarrow q \\equiv (p \\rightarrow q) \\wedge (q \\rightarrow p)$
        * $\\neg(p \\rightarrow q) \\equiv p \\wedge \\neg q$
        """
        )

    with col_b:
        st.markdown("### ⚖️ กฎการอ้างเหตุผลยอดฮิต")
        st.info(
            """
        * **Modus Ponens:** $p \\rightarrow q, p \\vdash q$
        * **Modus Tollens:** $p \\rightarrow q, \\neg q \\vdash \\neg p$
        * **Hypothetical Syllogism:** $p \\rightarrow q, q \\rightarrow r \\vdash p \\rightarrow r$
        * **Disjunctive Syllogism:** $p \\vee q, \\neg p \\vdash q$
        """
        )

    st.markdown("---")
    st.markdown("### 🔍 สมมูลของตัวบ่งปริมาณ")
    st.warning(
        """
    * $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$
    * $\\neg \\exists x P(x) \\equiv \\forall x \neg P(x)$
    """
    )
