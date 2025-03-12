import secrets
import string

def generate_strong_password(length=16):
    # تعريف المجموعات التي سيتم استخدامها في كلمة المرور
    lowercase_letters = string.ascii_lowercase  # الحروف الصغيرة (a-z)
    uppercase_letters = string.ascii_uppercase  # الحروف الكبيرة (A-Z)
    digits = string.digits                     # الأرقام (0-9)
    special_characters = string.punctuation    # الرموز الخاصة (!, @, #, $, ...)

    # دمج جميع المجموعات معًا
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # التأكد من أن كلمة المرور تحتوي على كل نوع من الأحرف (لزيادة الأمان)
    password = [
        secrets.choice(lowercase_letters),  # حرف صغير واحد على الأقل
        secrets.choice(uppercase_letters),  # حرف كبير واحد على الأقل
        secrets.choice(digits),             # رقم واحد على الأقل
        secrets.choice(special_characters)  # رمز خاص واحد على الأقل
    ]

    # إكمال باقي طول كلمة المرور بحروف وأرقام ورموز عشوائية
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # خلط الأحرف لضمان عدم وجود نمط ثابت
    secrets.SystemRandom().shuffle(password)

    # تحويل القائمة إلى سلسلة نصية وإرجاعها
    return ''.join(password)

# عرض البانر
def display_banner():
    banner = """
    ██████╗ ██╗   ██╗██╗     ██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██║   ██║██║     ██║ ██╔╝██╔══██╗╚══██╔══╝
    ██████╔╝██║   ██║██║     █████╔╝ ███████║   ██║   
    ██╔═══╝ ██║   ██║██║     ██╔═██╗ ██╔══██║   ██║   
    ██║     ╚██████╔╝███████╗██║  ██╗██║  ██║   ██║   
    ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    ==================== Madara_dz ====================
                         contact:
                My Discord: @Hunter_Sploit
     Github for support: https://github.com/HunterSploit
    """
    print(banner)

# توليد كلمة مرور قوية بطول 16 حرفًا
if __name__ == "__main__":
    display_banner()  # عرض البانر
    password = generate_strong_password(16)
    print("The Password is :", password)