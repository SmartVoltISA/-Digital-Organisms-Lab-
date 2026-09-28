# DOL-E003 — Physical interpretation of the c302 intervention

## What “physical” means here

DOL-E003 is **not a physical experiment on a living worm**.

It is a physical/mechanistic description of the dynamical substrate represented by the c302 C1 computational model. The simulation integrates membrane and ion-channel dynamics and an electrical coupling between two modeled cells.

The distinction is mandatory:

- **physical mechanism represented:** membrane voltage, ionic-channel state variables, electrical coupling current;
- **experimental substrate:** numerical simulation of those equations;
- **biological claim:** none beyond what is explicitly supported by the c302 model and its provenance.

## Relation under test

The tested relation is the bidirectional electrical coupling:

**AIZL ↔ ASHL**

In the NeuroML model, both directions are represented as electrical projections using:

`neuron_to_neuron_elec_syn`

with:

`conductance = 0.00052 nS`

For an electrical coupling, the conceptual current is proportional to the voltage difference between the coupled cells:

`I_gap ∝ g_gap (V_AIZL - V_ASHL)`

The exact current law used by the simulator/model definition is authoritative; the equation above is the physical interpretation of the coupling term, not a replacement for the model implementation.

## Physical intervention

### ON

The original electrical projections are present.

A perturbation is applied to AIZL using the existing 1 pA pulse:

- start: 500 ms
- duration: 800 ms

The question is whether the perturbation changes ASHL through the existing electrical coupling.

### CUT

Only the AIZL↔ASHL electrical relation is removed from the derived experiment.

No membrane parameters, ion-channel parameters, stimulus parameters, cell definitions, or unrelated connections are changed.

Mechanistically this asks:

> What part of the ASHL response disappears when the electrical pathway between AIZL and ASHL is unavailable?

### RESTORE

The exact original electrical projections and coupling strength are restored.

The same perturbation is then applied.

Mechanistically this asks whether the previously removed response pathway is recoverable by restoring the same relation.

## What is actually measured

The primary observable is ASHL membrane potential (V_{ASHL}(t)).

We compare its deviation from the pre-stimulus baseline during the fixed perturbation interval.

This is a local intervention measurement:

`AIZL perturbation → electrical coupling → ASHL voltage response`

The important quantity is not an absolute voltage value by itself, but the change caused by changing the relation.

## Physical controls

### Sham

Repeat the ON model without changing the relation.

This checks that the surgical preparation itself does not introduce a numerical change.

### Negative source

Apply the same type and timing of perturbation to AS2.

AS2 is not the selected endpoint of the AIZL↔ASHL electrical relation.

This tests whether an apparently similar response can arise without perturbing the tested source.

### Restoration

RESTORE is itself a causal control:

`ON → CUT → RESTORE`

A genuine relation-dependent effect should follow the intervention state rather than merely the passage of simulation time.

## What a PASS would physically mean

A PASS would mean:

> Within the specified c302 C1 dynamical model, changing only the AIZL↔ASHL electrical coupling changes the measured ASHL response to a matched AIZL perturbation, and restoring the coupling recovers that response within the preregistered tolerance.

That is a mechanistic statement about the tested model.

## What it would NOT mean

It would not mean:

- that a living C. elegans has been experimentally manipulated;
- that the exact conductance value is biologically correct;
- that AIZL↔ASHL is a universal example of relation in nature;
- that every biological synapse or electrical connection behaves identically;
- that the model proves a new physical law;
- that c302 is equivalent to the organism.

## Why this matters for DOL

DOL separates three levels that are often mixed together:

1. **Physical interpretation** — what mechanism the model represents.
2. **Computational experiment** — what intervention the simulator actually performs.
3. **Biological interpretation** — what, if anything, can be inferred about the living organism.

DOL-E003 is currently at level 1 + preregistered level 2.

Level 3 remains outside the experiment unless independently supported by biological evidence.

## Status

**PREREGISTERED / NOT RUN**

No physical or biological result is claimed until the numerical simulation is executed and its output is recorded.
