Trust = 0
Attachment = 0
Harmony = 0
Caution = 0
Intuition = 0

Memory = 0
Magic = 0
Awakening = 0
Balance = 0

with open("Привітання", "r", encoding="utf-8") as fil:
   print(fil.read())

with open("правила", "r", encoding="utf-8") as fil:
   print(fil.read())

with open("характиристики.txt", "r", encoding="utf-8") as fil:
   print(fil.read())
start = input("Натисни Enter, щоб почати гру...")

print("🌙 Сцена 1: Пробудження")

with open("сцена 1, кадр 1", "r", encoding="utf-8") as fil:
   print(fil.read())

van = input("🔸 Вибір:\n 1.🤲 Простягнути ручку до жінки \n2.🛌 Закрити очі й заховатись у ковдру \n3.🌟 Пошепки прошепотіти ім’я: Пушок")
if van == "1":
   print("\nТи повільно, невпевнено піднімаєш крихітну ручку. Вона тремтить — і торкається її пальців.")
   print("\nЖінка здригається від несподіваної ніжності.")
   print("— Вона… розуміє нас. Вона така особлива…")
   print("\nТи не можеш говорити. Але вона вже щось відчула.")
   print("У твоїх очах — глибина, не властива немовлятам.")
   print("\nВ її серці — щось стискається. Можливо… вона вже любить тебе по-справжньому.")
   print("\n🕊️ Внутрішній голос:\n«Вперше… я не боюсь довіри. Це дивно… але приємно.»")
   print("\n📌 [Довіра +1]")
   with open("xarakt.txt", "w",encoding="utf-8") as fp:
      fp.write("Trust = " + str(1) + "\n")
      fp.write("Attachment = " + str(0) + "\n")
      fp.write("Harmony = " + str(0) + "\n")
      fp.write("Caution = " + str(0) + "\n")
      fp.write("Intuition = " + str(0) + "\n")
      fp.write("Memory = " + str(0) + "\n")
      fp.write("Magic = " + str(0) + "\n")
      fp.write("Awakening = " + str(0) + "\n")
      fp.write("Balance = " + str(0) + "\n")
if van == "2":
   print("\nТи відчуваєш їхню присутність — теплу, світлу… занадто світлу.")
   print("Інстинкт старого життя бере гору: ти натягуєш ковдру до підборіддя і зариваєшся всередину.")
   print("\nЖінка засміялась:\n— О, вона сором’язлива.")
   print("Чоловік усміхнувся:\n— Або просто втомлена.")
   print("\nВони не тиснуть. Не силують. Просто поруч — чекають.")
   print("\n🕯️ Внутрішній голос:\n«Я завжди ховалась від почуттів. Але ці… не схожі на страх.»")
   print("\n📌 [Обачність +1]")
   with open("xarakt.txt", "w",encoding="utf-8") as fp:
      fp.write("Trust = " + str(0) + "\n")
      fp.write("Attachment = " + str(0) + "\n")
      fp.write("Harmony = " + str(0) + "\n")
      fp.write("Caution = " + str(1) + "\n")
      fp.write("Intuition = " + str(0) + "\n")
      fp.write("Memory = " + str(0) + "\n")
      fp.write("Magic = " + str(0) + "\n")
      fp.write("Awakening = " + str(0) + "\n")
      fp.write("Balance = " + str(0) + "\n")
if van == "3":
   print("\nЛедь чутно, майже подумки, ти вимовляєш ім’я.\n— …Пушок…")
   print("\nСвіт навколо ніби завмирає. Повітря на мить стає важчим.")
   print("Жінка насторожено нахиляється:\n— Що вона сказала?")
   print("\nАле ти вже мовчиш.")
   print("\nДесь далеко — за межами цього світу — твій брат-близнюк прокидається.")
   print("У нього стискається серце. Він чує тебе.")
   print("\n🌓 Внутрішній голос Пушка:\n«Анерам? Це ти? Що ти зробила…?»")
   print("\n🌀 У твоїй душі ворухнулась пам’ять.\nШепіт з минулого, дотик сил, що спали.")
   print("\n📌 [Пам’ять + 1]")
   with open("xarakt.txt", "w",encoding="utf-8") as fp:
      fp.write("Trust = " + str(0) + "\n")
      fp.write("Attachment = " + str(0) + "\n")
      fp.write("Harmony = " + str(0) + "\n")
      fp.write("Caution = " + str(0) + "\n")
      fp.write("Intuition = " + str(0) + "\n")
      fp.write("Memory = " + str(1) + "\n")
      fp.write("Magic = " + str(0) + "\n")
      fp.write("Awakening = " + str(0) + "\n")
      fp.write("Balance = " + str(0) + "\n")
else:
    print("Невідомий вибір.")






