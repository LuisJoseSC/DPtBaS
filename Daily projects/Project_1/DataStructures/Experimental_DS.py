from datetime import datetime

FILEPATH = "C:/Users/liyo0/OneDrive/Porgramacion/Repostories/DPtBaS/Daily projects/Project_1/Data/sessions.csv"

rows_validas = []
errores = []
filas_invalidas = 0
minutos_por_topic = {}

def parse_date(date_str: str) -> str:
    # Valida formato YYYY-MM-DD
    datetime.strptime(date_str, "%Y-%m-%d")
    return date_str

with open(FILEPATH, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    # Esperado: date,topic,minutes,score

    for lineno, line in enumerate(f, start=2):  # empieza en 2 por el header
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 4:
            filas_invalidas += 1
            errores.append(f"L{lineno}: columnas != 4 -> {line!r}")
            continue

        date_s, topic, minutes_s, score_s = parts

        try:
            # Validaciones
            parse_date(date_s)

            minutes = int(minutes_s)
            if minutes <= 0:
                raise ValueError(f"minutes <= 0 ({minutes})")

            score = float(score_s)
            if not (0.0 <= score <= 5.0):
                raise ValueError(f"score fuera de rango [0,5] ({score})")

            # Construcción dict
            row = {
                "date": date_s,
                "topic": topic,
                "minutes": minutes,
                "score": score,
            }
            rows_validas.append(row)

            # Acumulación por topic
            minutos_por_topic[topic] = minutos_por_topic.get(topic, 0) + minutes

        except Exception as e:
            filas_invalidas += 1
            errores.append(f"L{lineno}: {type(e).__name__}: {e} -> {line!r}")
            continue

print("Minutos por topic:")
for topic, total in sorted(minutos_por_topic.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {topic}: {total}")

print("\nFilas inválidas:", filas_invalidas)

print("\nErrores detectados:")
for err in errores:
    print(" ", err)
