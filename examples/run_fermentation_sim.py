from src.fermentation_compute import YeastNode

node = YeastNode(capacity=10)
work_done = node.feed_substrate(8.0)

print(f"Fed 8 units of substrate. Work processed: {work_done}")
print(f"Node metabolic fatigue (ethanol): {round(node.ethanol_concentration, 2)}")
