import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri yükleme
df = pd.read_csv("daily_weather.csv", parse_dates=["Tarih"])

# Genel istatistikler
print("📈 Temel İstatistikler:\n", df.describe())

# Zaman serisi görselleştirme
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Tarih", y="Sıcaklık (C)", label="Sıcaklık")
sns.lineplot(data=df, x="Tarih", y="Nem (%)", label="Nem")
plt.title("10 Günlük Hava Durumu Analizi")
plt.xlabel("Tarih")
plt.ylabel("Değer")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Korelasyon analizi
correlation = df[["Sıcaklık (C)", "Nem (%)", "Rüzgar Hızı (km/h)"]].corr()
print("\n🔗 Korelasyon Matrisi:\n", correlation)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Değişkenler Arası Korelasyon")
plt.show()
