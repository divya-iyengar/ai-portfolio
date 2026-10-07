# Nissan Advanced Technology Center

## Role

Autonomous Driving Planner Research Engineer
April 2025 - Present

## Summary 
I work on research and development for the autonomous driving behavior prediction and planning team, with a focus on improving decision making at complex urban intersections. My work bridges traditional rules-based approaches and machine learning by investigating how learned models can improve ego vehicle predictions while remaining compatible with the existing planning architectures.

The role combines software engineering, robotics, machine learning, and systems thinking. In addition to developing new algorithms, I evaluate planner behavior, investigate failure modes, design validation experiments, and communicate technical results to engineers and stakeholders globally.


## Key Contributions

### Machine Learning for Intersection Decision Making

Designed and developed an end-to-end machine learning pipeline to predict intersection occupancy and support planner decision making in scenarios where rules-based logic struggles, such as ambiguous right-of-way interactions and partially occluded environments. 

Responsibilities included:
- Defining the learning problem and prediction targets
- Designing temporal and interaction-based feature representations
- Developing data preprocessing and labeling pipelines
- Implementing Transformer-based neural network architectures in PyTorch
- Building a multi-agent representation via graph neural networks in PyTorch
- Training, validating, and evaluating models on recorded driving scenarios
- Comparing learned behavior against existing planner logic

### Data Pipeline Development

Developed tooling to transform autonomous driving logs into machine learning datasets.

Work included:
- sequence generation
- feature engineering
- label generation
- dataset balancing 
- experiment management
- visualization and debugging

The resulting datasets enabled rapid experimentation across multiple model architectures and training configurations.

### Planner Investigation and Debugging

Investigated planner behaviors by tracing decisions through the planning stack, identifying failure modes, and determining whether issues originated from perception, prediction, planning logic, controller behavior, or downstream integration. 

Implemented software improvements that resolved planner edge cases while maintaining compatibility with existing system behavior.

### Research Communication

Prepared technical presentations summarizing research direction, experimental methodology, model architectures, and validation results for internal engineering stakeholders.

Presented technical tradeoffs between different machine learning approaches, including discussion of future research directions. Supported both Japan and US research focuses.  


## Technologies

Programming Languages
- Python
- C++

Machine Learning
- PyTorch
- Transformer architectures (encoder)
- Sequence modeling
- Supervised learning
- Graph Neural Network Architectures (R-GCN)

Robotics
- ROS
- Autonomous vehicle planning
- Motion planning
- Behavior planning

Development
- Git
- Linux

## Challenges

One recurring challenge was balancing improvements from machine learning with the practical contraints of an existing planning system. Rather than replacing decision making logic outright, proposed solutions needed to integrate with established architecture, operate reliably across diverse driving scenarios, and provide measurable improvements without introducing unacceptable regressions or overrides.

Another challenge involved highly imbalanced datasets and long-tail driving scenarios. Rare but safety-critical behaviors required careful dataset design, feature engineering, and evaluation strategies to ensure models generalized beyond the most common traffic situations.

## Lessons Learned

Working on autonomous driving reinforced that successful AI systems require much more than model development. Data quality, feature representation, evaluation methodology, software integration, and system validation often have a greater impact on real-world performance than incremental improvements in model architecture. The role also increased my appreciation for designing AI systems as components within larger software platforms. 