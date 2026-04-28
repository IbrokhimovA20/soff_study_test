n_range = np.linspace(2000, 6000, 1000)
def stability_limit(n):
    lobes = 1.5 + 0.3 * np.sin(n/200) + 0.2 * np.cos(n/50)
    boundary = np.where((n > 2700) & (n < 3300), lobes - 0.7, lobes)
    boundary = np.where((n > 4200) & (n < 4800), boundary - 0.5, boundary)
    return boundary

plt.figure(figsize=(12, 7))
limit = stability_limit(n_range)
plt.fill_between(n_range, 0.5, limit, color='honeydew', label='Stable Zone')
plt.fill_between(n_range, limit, 2.5, color='mistyrose', label='Нестабильная зона (Вибрация)')
plt.plot(n_range, limit, 'k-', linewidth=1.5)

plt.scatter([3000], [1.5], c='red', s=100, edgecolors='k', label='Мода 1 (Нестабильная)')
plt.scatter([4500], [1.0], c='blue', s=100, edgecolors='k', label='Mode 2 (Near Limit)')
opt_n = [2400, 3700, 5300, 5800]
opt_ap = [1.2, 1.5, 1.3, 1.1]
plt.plot(opt_n, opt_ap, 'go--', markersize=10, label='Мода 3 (Оптимизированный путь)')

plt.title('Диаграмма стабильности')
plt.xlabel('Spindle Speed (rpm)')
plt.ylabel('Глубина резания (мм)')
plt.ylim(0.5, 2.5)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()