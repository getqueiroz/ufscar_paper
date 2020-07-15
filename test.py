import selector
import feature

# TEST 1
candidates = ["Gun", "Bell"];
s1 = selector.Selector(candidates)

f1 = feature.Feature("Applicator Cost", 5)
s1.add_ndn_measurable_feature(f1, feature.Mode.MINIMAZING, [120e3, 140e3])

f2 = feature.Feature("Safety Issues", 5)
s1.add_immeasurable_feature(f2, [4, 3])

s1.calc_premium_values()

# TEST 2
candidates = ["Gun", "Bell"]
s2 = selector.Selector(candidates)

f1 = feature.Feature("Transfer Efficiency", 3)
s2.add_immeasurable_feature(f1, [2, 4])

f2 = feature.Feature("Part Ground Sensitivity", 2)
s2.add_immeasurable_feature(f2, [4, 2])

f3 = feature.Feature("Penetration Into Dificult Areas", 2)
s2.add_immeasurable_feature(f3, [4, 1])

f4 = feature.Feature("Ease of Path Teaching", 3)
s2.add_immeasurable_feature(f4, [2, 4])

f5 = feature.Feature("Atomized Particle Size", 2)
s2.add_immeasurable_feature(f5, [3, 4])

f6 = feature.Feature("Applicator Cost", 5)
s2.add_ndn_measurable_feature(f6, feature.Mode.MINIMAZING, [120e3, 140e3])

f7 = feature.Feature("Energy Consuption", 5)
s2.add_dv_measurable_feature(f7, 14, feature.Mode.MINIMAZING, [20, 15])

f8 = feature.Feature("Finish Quality", 4)
s2.add_immeasurable_feature(f8, [3, 4])

f9 = feature.Feature("Safety Issues", 5)
s2.add_immeasurable_feature(f9, [4, 3])

f10 = feature.Feature("Fire Protection", 1)
s2.add_immeasurable_feature(f10, [4, 2])

f11 = feature.Feature("Spare Parts Cost", 5)
s2.add_dv_measurable_feature(f11, 800, feature.Mode.MINIMAZING, [1200, 1900])

s2.calc_premium_values()