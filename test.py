import selector
import feature

# TEST 1
candidates = ["Gun", "Bell"];
s = selector.Selector(candidates)

f1 = feature.Feature("Applicator Cost", 5)
s.add_ndn_measurable_feature(f1, feature.Mode.MINIMAZING, [120e3, 140e3])

f2 = feature.Feature("Safety Issues", 5)
s.add_immeasurable_feature(f2, [4, 3])

s.calc_premium_values()

# TEST 2
candidates = ["Gun", "Bell"]
s = selector.Selector(candidates)

f1 = feature.Feature("Atomized Particle Size", 2)
s.add_immeasurable_feature(f1, [3, 4])

f2 = feature.Feature("Applicator Cost", 5)
s.add_ndn_measurable_feature(f2, feature.Mode.MINIMAZING, [120e3, 140e4])

f3 = feature.Feature("Energy Consuption", 5)
s.add_dv_measurable_feature(f3, 14, feature.Mode.MINIMAZING, [20, 15])

f4 = feature.Feature("Finish Quality", 4)
s.add_immeasurable_feature(f4, [3, 4])

s.calc_premium_values()