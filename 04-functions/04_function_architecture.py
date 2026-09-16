"""
Module: 04_function_architecture.py
Description: Functional design, dynamic arguments (*args, **kwargs), pure functions, and scope concepts.
Unit: 04 - Functions & Function Design
"""

# --- 1. Pure Functions & Default Arguments (الدرس 14 & 15 & 19) ---
def clean_prompt_text(text):
    """تطهير النصوص وتنظيف المسافات الزائدة."""
    if not text:
        return ""
    return text.strip().lower()


def calculate_token_cost(token_count, cost_per_token=0.00002):
    """حساب التكلفة باستخدام Positional & Default arguments."""
    return token_count * cost_per_token


# --- 2. Dynamic Arguments (*args & **kwargs) & Unpacking (الدرس 16) ---
def build_llm_payload(model_name, system_prompt, *user_messages, **model_params):
    """
    بناء هيكل البيانات باستخدام *args لاستقبال عدة رسائل 
    و **kwargs لاستقبال إعدادات النموذج الشارحة.
    """
    clean_system = clean_prompt_text(system_prompt)
    
    # تجميع الرسائل القادمة عبر *args
    messages_list = [{"role": "system", "content": clean_system}]
    
    for msg in user_messages:
        if msg:
            messages_list.append({"role": "user", "content": clean_prompt_text(msg)})
    
    # إنشاء الدكشنري الأساسي للطلب
    payload = {
        "model": model_name,
        "messages": messages_list,
        "config": model_params  # استقبال الـ **kwargs
    }
    return payload


# --- 3. Functions as Objects & Higher-Order Functions (الدرس 18) ---
def process_text_pipeline(raw_text, transform_function):
    """دالة تستقبل دالة أخرى كـ argument وتنفذها (Functions as objects)."""
    return transform_function(raw_text)


# --- 4. Execution & Unpacking Simulation (الدرس 16 & 18) ---
print("=" * 60)
print("LLM PAYLOAD BUILDER (Dynamic Arguments & Pure Functions)")
print("=" * 60)

# تفكيك الدكشنري كـ Keyword Arguments (**kwargs unpacking)
runtime_config = {"temperature": 0.2, "max_tokens": 150}

# استدعاء الدالة بدمج Positional, *args, و **kwargs
payload = build_llm_payload(
    "gpt-4o",
    " YOU ARE AN AI AUTOMATION ASSISTANT. ",
    "Extract all email domains.",
    "Process this file.",
    **runtime_config
)

print(f"Target Model       : {payload['model']}")
print(f"System Message     : {payload['messages'][0]['content']}")
print(f"Total Messages     : {len(payload['messages'])}")
print(f"Runtime Parameters : {payload['config']}")

# استخدام Lambda والدوال كأجسام (First-class functions)
raw_ai_output = "   SUCCESS: PROCESSED 42 RECORDS   "

# تمرير دالة عادية
step1_result = process_text_pipeline(raw_ai_output, clean_prompt_text)

# تمرير Lambda function للتنسيق
final_result = process_text_pipeline(step1_result, lambda text: text.upper())

print("\n" + "=" * 60)
print("FUNCTION AS OBJECT & LAMBDA DEMO")
print("=" * 60)
print(f"Raw Input     : '{raw_ai_output}'")
print(f"Final Processed: '{final_result}'")

# فرز القوائم باستخدام sorted() و lambda (الدرس 18)
execution_times = [
    {"task": "data_extract", "ms": 230},
    {"task": "api_dispatch", "ms": 110},
    {"task": "db_insert", "ms": 450}
]

sorted_tasks = sorted(execution_times, key=lambda item: item["ms"])
print(f"\nFastest Task : {sorted_tasks[0]['task']} ({sorted_tasks[0]['ms']}ms)")
print("=" * 60)