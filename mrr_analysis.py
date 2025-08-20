# mrr_analysis.py
import matplotlib.pyplot as plt

# Quarterly MRR Growth Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [8.24, 3.27, 11.56, 13.12]
industry_target = 15

# Calculate average
average_mrr = sum(mrr_growth)/len(mrr_growth)
print(f"Average MRR Growth: {average_mrr:.2f}")  # 9.05

# Visualization
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label='Company MRR Growth')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (15)')
plt.title("SaaS MRR Growth vs Industry Benchmark")
plt.ylabel("MRR Growth (%)")
plt.xlabel("Quarter")
plt.ylim(0, max(industry_target+5, max(mrr_growth)+5))
plt.grid(True)
plt.legend()
plt.savefig("mrr_growth_chart.png")
plt.show()
