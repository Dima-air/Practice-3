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

def get_normal(char, names):
    normal = []
    base = char[0]
    for item in char:
        row = []
        for i in range(len(item)):
            if names[i] == "Вес (кг)":
                row.append(base[i] / item[i])
            else:
                row.append(item[i] / base[i])
        normal.append(row)
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
    plt.xticks(rotation=15, ha="right", fontsize=8)
    plt.tight_layout()
    plt.show()

def create_radial(models, name, values):
    plot_values = [v + v[:1] for v in values]
    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(plot_values)):
        ax.plot(angles, plot_values[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=8)
    ax.set_ylim(0, max([max(v) for v in plot_values]) + 0.2)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик", pad=20)
    plt.show()


normalized_data = get_normal(char, name_char)
data = get_quality(normalized_data)
create_bar(models, data)
create_radial(models, name_char, normalized_data)