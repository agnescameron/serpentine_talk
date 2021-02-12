# Pfeifer Intro

Rolf Pfeifer's Symbols, Patterns and Behaviour: Towards a New Understanding of Intelligence is a paper that has had a strong influence on how I think about 'artificial intelligence'. In it, Pfeifer makes a case that what we observe as intelligent behaviour (or not) is a function of perspective, and that all behaviour is fundamentally defined at the interface between an agent and its environment.

The title invokes 3 contrasting models by which we understand intelligence: that it is based on symbol-processing capacity (e.g. early chess computers), that it relies on pattern recognition (e.g. neural networks), or that it is, as Pfeifer contends, ultimately located somewhere in the relationship of a body with the wider world.

The paper gives a class of principles for designing agents that exhibit this embodied intelligence, placing an emphasis on autonomy, situatedness (agents control their interactions with the environment), and tight sensory-motor co-ordination (rather than viewing sensing and acting as separate 'modules' controlled by a central processor). Their final principle, that of 'good design is cheap' is one that feels particularly apt for a discussion around intelligence and interfaces:

"Leg coordination in insects does not require a central controller. There is no internal process corresponding to global communication between the legs... but there is global communication between all the legs, namely through the environment. It is mediated by a physical process, not by an information process (or a process of signal transfer) within the agent. If the insect lifts one leg, the force on all other legs is changed instantaneously because of the weight of the insect."

This example - of an intelligence wholly dependent on an interface with the environment, where apparently complex behaviour is undergirded by simple physical processes not requiring "unnecessary neural substrate" (in later work, this is termed "morphological computation" (1)) - runs counter to models that emphasise information-processing as the key to intelligent systems.

Despite being written in 1996, many of the arguments in the paper ring true today. For example, the problem of 'symbol grounding' - the idea that in order for an agent to deal effectively with abstract concepts, they must be grounded in that agents' interaction with the real world - is one we still encounter with pattern-matching machine learning systems. Given recent accidents involving self-driving cars, where the vehicles fail to adequately apply human labels to an unexpected and shifting set of circumstances (2), and still struggle in sensorially confusing conditions like rain and snow (3), it's interesting to think about how a more embodied approach to intelligence would change the way we talk about these problems.


1. Rolf Pfeifer; Fumiya Iida; Gabriel Gómez (2006). Morphological computation for adaptive behavior and cognition. , 1291(none), 0–29. doi:10.1016/j.ics.2005.12.080  

2. Timothy B Lee, How terrible software design decisions led to Uber's deadly 2018 crash, https://arstechnica.com/cars/2019/11/how-terrible-software-design-decisions-led-to-ubers-deadly-2018-crash/

3. Van Brummelen, Jessica; O'Brien, Marie; Gruyer, Dominique; Najjaran, Homayoun (2018). Autonomous vehicle perception: The technology of today and tomorrow. Transportation Research Part C: Emerging Technologies, (), S0968090X18302134–. doi:10.1016/j.trc.2018.02.012  
