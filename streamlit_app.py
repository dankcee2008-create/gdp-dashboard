import streamlit as st

# ─────────────────────────────────────────────
#  QUESTION BANK  — add more dicts to this list
# ─────────────────────────────────────────────
QUESTIONS = [
    {
        "question": "What is the output of: `type([])` in Python?",
        "options": ["<class 'tuple'>", "<class 'dict'>", "<class 'list'>", "<class 'set'>"],
        "answer": "<class 'list'>",
        "explanation": "`[]` creates an empty list, so `type([])` returns `<class 'list'>`.",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def",
        "explanation": "Python uses the `def` keyword to define functions.",
    },
    {
        "question": "What does `len({'a': 1, 'b': 2, 'c': 3})` return?",
        "options": ["6", "2", "3", "Error"],
        "answer": "3",
        "explanation": "`len()` on a dict returns the number of key-value pairs — here that's 3.",
    },
    {
        "question": "Which of these is an immutable data type in Python?",
        "options": ["list", "dict", "set", "tuple"],
        "answer": "tuple",
        "explanation": "Tuples are immutable; once created their elements cannot be changed.",
    },
    {
        "question": "What is the correct way to create an empty set?",
        "options": ["{}", "set()", "[]", "()"],
        "answer": "set()",
        "explanation": "`{}` creates an empty dict, not a set. Use `set()` for an empty set.",
    },
    {
        "question": "What does the `*args` syntax allow in a Python function?",
        "options": [
            "Only keyword arguments",
            "A fixed number of arguments",
            "An arbitrary number of positional arguments",
            "An arbitrary number of keyword arguments",
        ],
        "answer": "An arbitrary number of positional arguments",
        "explanation": "`*args` collects extra positional arguments into a tuple.",
    },
    {
        "question": "Which method removes and returns the last item of a list?",
        "options": ["remove()", "delete()", "pop()", "discard()"],
        "answer": "pop()",
        "explanation": "`list.pop()` removes and returns the last element by default.",
    },
    {
        "question": "What is the output of `2 ** 10`?",
        "options": ["20", "100", "512", "1024"],
        "answer": "1024",
        "explanation": "`**` is the exponentiation operator. 2¹⁰ = 1024.",
    },
    {
        "question": "Which built-in function returns a sorted list from an iterable?",
        "options": ["sort()", "sorted()", "order()", "arrange()"],
        "answer": "sorted()",
        "explanation": "`sorted()` returns a new sorted list; `.sort()` sorts a list in-place.",
    },
    {
        "question": "What does `range(1, 10, 2)` produce?",
        "options": [
            "[1, 2, 3, 4, 5, 6, 7, 8, 9]",
            "[1, 3, 5, 7, 9]",
            "[2, 4, 6, 8, 10]",
            "[1, 3, 5, 7, 9, 11]",
        ],
        "answer": "[1, 3, 5, 7, 9]",
        "explanation": "`range(start, stop, step)` — starts at 1, stops before 10, steps by 2.",
    },
    {
        "question": "Which statement about Python lists is TRUE?",
        "options": [
            "Lists are immutable",
            "Lists can only store integers",
            "Lists are ordered and allow duplicates",
            "Lists use curly braces {}",
        ],
        "answer": "Lists are ordered and allow duplicates",
        "explanation": "Python lists maintain insertion order and allow duplicate values.",
    },
    {
        "question": "What is a lambda function?",
        "options": [
            "A function that runs on a separate thread",
            "An anonymous one-line function",
            "A recursive function",
            "A built-in Python function",
        ],
        "answer": "An anonymous one-line function",
        "explanation": "`lambda` creates small anonymous functions: `lambda x: x * 2`.",
    },
]

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Python Quiz 🐍",
    page_icon="🐍",
    layout="centered",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

    /* hide default streamlit chrome */
    #MainMenu, footer { visibility: hidden; }

    .quiz-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem 1.5rem;
        margin-bottom: 1.5rem;
        color: white;
    }
    .quiz-header h1 {
        font-family: 'Syne', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 0.25rem;
        color: white;
    }
    .quiz-header p { margin: 0; opacity: 0.7; font-size: 0.95rem; }

    .question-card {
        background: white;
        border: 1px solid #e8e5df;
        border-radius: 14px;
        padding: 1.75rem 2rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }
    .question-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #e84855;
        margin-bottom: 0.5rem;
    }
    .question-text {
        font-family: 'Syne', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.4;
    }

    /* score pill */
    .score-pill {
        display: inline-block;
        background: #eaf3de;
        color: #3b6d11;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 4px 14px;
        border-radius: 20px;
        margin-top: 0.5rem;
    }

    /* feedback boxes */
    .feedback-correct {
        background: #eaf3de;
        border-left: 4px solid #639922;
        border-radius: 8px;
        padding: 0.85rem 1rem;
        color: #27500a;
        font-size: 0.9rem;
        margin-top: 0.75rem;
    }
    .feedback-wrong {
        background: #fcebeb;
        border-left: 4px solid #e24b4a;
        border-radius: 8px;
        padding: 0.85rem 1rem;
        color: #501313;
        font-size: 0.9rem;
        margin-top: 0.75rem;
    }

    /* result card */
    .result-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #3d5a80 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 1.5rem;
    }
    .result-card h2 {
        font-family: 'Syne', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: white;
    }
    .result-card .big-score {
        font-family: 'Syne', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        line-height: 1;
        margin: 0.5rem 0;
    }
    .grade-badge {
        display: inline-block;
        padding: 6px 20px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 0.5rem;
    }

    /* review items */
    .review-item {
        background: white;
        border: 1px solid #e8e5df;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .review-item .rq { font-weight: 600; font-size: 0.92rem; color: #1a1a2e; margin-bottom: 0.3rem; }
    .review-item .ra { font-size: 0.83rem; color: #5f5e5a; }
    .review-item .ra .correct-ans { color: #3b6d11; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
#  SESSION STATE INITIALISATION
# ─────────────────────────────────────────────
def init_state():
    defaults = {
        "current_q": 0,          # index of current question
        "score": 0,              # running tally
        "answered": False,       # has user picked an answer this round?
        "selected": None,        # which option they picked
        "user_answers": [],      # list of dicts for review screen
        "quiz_done": False,      # are we on the results page?
        "started": False,        # have they passed the welcome screen?
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

total_questions = len(QUESTIONS)

# ─────────────────────────────────────────────
#  HELPER: grade
# ─────────────────────────────────────────────
def get_grade(pct):
    if pct >= 90: return "A+", "#eaf3de", "#3b6d11"
    if pct >= 80: return "A",  "#eaf3de", "#3b6d11"
    if pct >= 70: return "B",  "#e6f1fb", "#0c447c"
    if pct >= 60: return "C",  "#faeeda", "#854f0b"
    if pct >= 50: return "D",  "#faeeda", "#854f0b"
    return "F", "#fcebeb", "#a32d2d"

# ─────────────────────────────────────────────
#  SCREEN 1 — WELCOME
# ─────────────────────────────────────────────
if not st.session_state.started and not st.session_state.quiz_done:
    st.markdown(
        """
        <div class="quiz-header">
            <h1>🐍 Python Quiz</h1>
            <p>Test your Python knowledge across data types, functions, and more.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3)
    col1.metric("Questions", total_questions)
    col2.metric("Options each", "4")
    col3.metric("Feedback", "Instant")

    st.markdown("#### Topics covered")
    st.markdown(
        "- Data types & structures (list, dict, tuple, set)\n"
        "- Functions (`def`, `lambda`, `*args`)\n"
        "- Built-in functions & operators\n"
        "- Control flow & ranges"
    )
    st.divider()
    if st.button("▶ Start Quiz", use_container_width=True, type="primary"):
        st.session_state.started = True
        st.rerun()

# ─────────────────────────────────────────────
#  SCREEN 2 — QUESTION
# ─────────────────────────────────────────────
elif st.session_state.started and not st.session_state.quiz_done:
    idx   = st.session_state.current_q
    q     = QUESTIONS[idx]

    # ── header ──
    st.markdown(
        f"""
        <div class="quiz-header">
            <h1>🐍 Python Quiz</h1>
            <p>Answer every question to see your final score.</p>
            <span class="score-pill">Score: {st.session_state.score} / {total_questions}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── progress bar ──
    progress_pct = idx / total_questions
    st.progress(progress_pct, text=f"Question {idx + 1} of {total_questions}")

    # ── question card ──
    st.markdown(
        f"""
        <div class="question-card">
            <div class="question-label">Question {idx + 1}</div>
            <div class="question-text">{q['question']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── options ──
    if not st.session_state.answered:
        for option in q["options"]:
            if st.button(option, key=f"opt_{idx}_{option}", use_container_width=True):
                st.session_state.selected  = option
                st.session_state.answered  = True
                correct = option == q["answer"]
                if correct:
                    st.session_state.score += 1
                st.session_state.user_answers.append({
                    "question":    q["question"],
                    "selected":    option,
                    "answer":      q["answer"],
                    "correct":     correct,
                    "explanation": q["explanation"],
                })
                st.rerun()
    else:
        # show disabled-style options with highlight
        selected = st.session_state.selected
        correct  = q["answer"]
        for option in q["options"]:
            if option == correct:
                st.success(f"✅  {option}", icon=None)
            elif option == selected:
                st.error(f"❌  {option}", icon=None)
            else:
                st.button(option, key=f"dis_{idx}_{option}", disabled=True, use_container_width=True)

        # feedback / explanation
        if selected == correct:
            st.markdown(
                f'<div class="feedback-correct">✔ Correct! {q["explanation"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="feedback-wrong">✘ Not quite. The correct answer is <strong>{correct}</strong>.<br>{q["explanation"]}</div>',
                unsafe_allow_html=True,
            )

        st.divider()

        # ── NEXT button ──
        is_last = idx == total_questions - 1
        btn_label = "🏁 See Results" if is_last else "Next Question →"
        if st.button(btn_label, use_container_width=True, type="primary"):
            if is_last:
                st.session_state.quiz_done = True
            else:
                st.session_state.current_q += 1
                st.session_state.answered  = False
                st.session_state.selected  = None
            st.rerun()

# ─────────────────────────────────────────────
#  SCREEN 3 — RESULTS
# ─────────────────────────────────────────────
elif st.session_state.quiz_done:
    score = st.session_state.score
    pct   = round((score / total_questions) * 100)
    grade, g_bg, g_color = get_grade(pct)

    # 🎈 balloons!
    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">
            <h2>Quiz Complete! 🎉</h2>
            <div class="big-score">{score}/{total_questions}</div>
            <p style="opacity:0.8; margin:0.25rem 0;">You scored {pct}%</p>
            <span class="grade-badge" style="background:{g_bg}; color:{g_color};">
                Grade: {grade}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # quick stats
    wrong = total_questions - score
    c1, c2, c3 = st.columns(3)
    c1.metric("✅ Correct",   score)
    c2.metric("❌ Wrong",     wrong)
    c3.metric("📊 Accuracy",  f"{pct}%")

    # ── answer review ──
    st.markdown("### 📋 Answer Review")
    for i, record in enumerate(st.session_state.user_answers, 1):
        icon = "✅" if record["correct"] else "❌"
        with st.expander(f"{icon}  Q{i}: {record['question'][:60]}{'…' if len(record['question'])>60 else ''}"):
            if record["correct"]:
                st.success(f"Your answer: **{record['selected']}** — Correct!")
            else:
                st.error(f"Your answer: **{record['selected']}**")
                st.success(f"Correct answer: **{record['answer']}**")
            st.info(f"💡 {record['explanation']}")

    st.divider()

    # restart
    if st.button("🔄 Try Again", use_container_width=True, type="primary"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun() 
        