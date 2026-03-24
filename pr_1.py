import matplotlib.pyplot as plt
import numpy as np

electric_scooters_detailed = {
    "Kugoo Kirin M5": {
        "Максимальная скорость (км/ч)": 55,
        "Запас хода (км)": 60,
        "Мощность мотора (Вт)": 1000,
        "Ёмкость батареи (Ач)": 21,
        "Вес (кг)": 35,
        "Максимальная нагрузка (кг)": 150
    },
    "Ninebot Max G30": {
        "Максимальная скорость (км/ч)": 30,
        "Запас хода (км)": 65,
        "Мощность мотора (Вт)": 350,
        "Ёмкость батареи (Ач)": 15,
        "Вес (кг)": 19.2,
        "Максимальная нагрузка (кг)": 100
    },
    "Xiaomi Mi Electric Scooter Pro 2": {
        "Максимальная скорость (км/ч)": 25,
        "Запас хода (км)": 45,
        "Мощность мотора (Вт)": 300,
        "Ёмкость батареи (Ач)": 12.8,
        "Вес (кг)": 14.2,
        "Максимальная нагрузка (кг)": 100
    },
    "Halten RS-02": {
        "Максимальная скорость (км/ч)": 40,
        "Запас хода (км)": 50,
        "Мощность мотора (Вт)": 800,
        "Ёмкость батареи (Ач)": 18,
        "Вес (кг)": 28,
        "Максимальная нагрузка (кг)": 130
    }
}

models = list(electric_scooters_detailed.keys())
name_char = list(electric_scooters_detailed[models[0]].keys())
char = [list(scooter.values()) for scooter in electric_scooters_detailed.values()]

def get_normal(char):
    normal = []
    for item in char:
        normal.append([a / b for a, b in zip(item, char[0])])
    return normal

def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result

def create_bar(name, values):
    plt.bar(name, values)
    plt.xlabel("Модель")
    plt.ylabel("Kту")
    plt.legend()
    plt.xticks(rotation=15, ha="right", fontsize=8)
    plt.tight_layout()
    plt.show()

def create_radial(models, name, values):
    for item in values:
        item += item[:1]

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values)):
        ax.plot(angles, values[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=8)
    ax.set_ylim(0, max([max(v) for v in values]) + 0.2)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик", pad=20)
    plt.show()

data = get_quality(get_normal(char))
create_bar(models, data)
create_radial(models, name_char, get_normal(char))