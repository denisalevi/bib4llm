# Citation Key: Cook - 2023 - A Geometric Framework for Odor Representation

---

# A Geometric Framework for Odor Representation

###### Jack A. Cook and Thomas A. Cleland


###### Dept. Psychology, Cornell University, Ithaca, NY 14853, USA

 Abstract


We present a generalized theoretical framework for olfactory representation and plasticity, using the theory of smooth manifolds and sheaves to depict categorical odor learning
via distributed neural computation. Beginning with the space of all possible inputs to
the olfactory system, we develop a dynamic model for odor learning that culminates
in a perceptual space in which categorical odor representations are hierarchically constructed through experience, exhibiting statistically appropriate consequential regions
and clear relationships between the broader and narrower identities to which a given
odor might be assigned. The model reflects both the sampling-based physical similarity
relationships among odorants, as observed in physiological receptor response profiles,
and the acquired, learning-dependent perceptual similarity relationships among odors
that can be measured behaviorally, and defines the relationship between them. Individual training and experience generates correspondingly more sophisticated odor identification capabilities. Because these odor representations are constructed from experience
and depend on local, distributed plasticity mechanisms, geometries that fix curvature are
insufficient to describe the capabilities of the system. This generative framework also
encompasses hypotheses explaining representational drift in postbulbar circuits and the
context-dependent remapping of perceptual similarity relationships.

**Keywords: set theory, contrast models, representational drift, olfactory bulb, category**
learning, topological spaces, geometry


###### Introduction

The task of sensory systems is to provide organisms with reliable, actionable information about their environments. However, useful information is not readily available; the
environmental features that are ecologically relevant to an organism are rarely directly
evident in primary receptor activation patterns. Rather, these representations of interest must be constructed from the combined signals of populations of sensory receptors.
This construction process is mediated by sophisticated networks of neural circuitry that
draw out different aspects of potentially important information from raw sensory input
patterns. (We previously have proposed that these interactions and transformations are
most effectively modeled as a cascade of successive representations [1, 2], in which each neuronal ensemble constructs its representation by selectively sampling the activity of its


1


-----

antecedents). With sufficient understanding of a given sensory modality, and of the neuronal architecture of the corresponding sensory system, these representations and their
transformations can be geometrically modeled.
Importantly, such vetted geometries sharply constrain how sensory representations
can be physically encoded and transformed by neuronal circuitry. For example, the high
dimensionality of odorant similarity space during sampling establishes that contrast enhancement transformations operating in this similarity space [3] cannot be mediated by
nearest-neighbor lateral inhibition, as once was believed, but instead require novel circuit mechanisms within the olfactory bulb that are able to embed and transform highdimensional features [4, 5]. That is, these fundamentally mathematical constraints concretely govern the architecture and function of neural circuits in the brain. Establishing
the geometries of representational cascades is foundational to understanding how the
underlying neural systems compute.
The representational cascade that underlies odor recognition and identification is impressively powerful and compact. Olfactory bulb circuits (Fig. 1) impose an internally
generated temporal structure on afferent inputs [6–11] while also regulating contrast [4,
5], normalizing neuronal activity levels [2, 12–16], governing interareal communication

[17, 18], and managing patterns of synaptic and structural plasticity [19–25]. The resulting perceptual system learns rapidly and is conspicuously resistant to retroactive and
compound interference [26, 27], as well as to interference from simultaneously encountered competing odorants (modeled in [28]), which can profoundly degrade the odorantspecific receptor activity profiles upon which odor recognition ostensibly depends [29–
33]. These capacities accentuate the implications of the profound plasticity of the early
olfactory system: odor representations, and the basic process of olfactory perception itself, are fundamentally and critically dependent on learning [34–36]. Discrete, meaningful odors and their implications – excepting a few species-specific innately recognizable
odors – must be categorically learned through individual experience. Indeed, there is
abundant evidence for the perceptual learning of meaningful odor representations, from
their generalization properties [13, 37], to the mechanisms of odor learning and memory

[24, 34, 38–42], to the association of odor representations with meaning and context, even
in peripheral networks such as the olfactory bulb [35, 43–51]. What we lack is a common
theoretical framework in which these diverse phenomena can be usefully embedded.

###### Perceptual frameworks

Theoretical frameworks for understanding sensory systems include perceptual spaces and
_hierarchical structures[1]. Both are founded on metrics of similarity [53–57], though the for-_
mer presumes an essentially continuous theoretical space of some dimensionality into
which individual stimulus representations are deployed, whereas the latter presumes
some degree of qualitative category membership for each such representation, with intercategory similarities mapping to the hierarchical proximities among categories. Perceptual spaces can be defined using a variety of metrics, including both physical metrics such
as wavelength (color) or frequency (pitch) and perceptual metrics such as those revealed

1Also see Semantic similarity and contrast models section, below

2


-----

![](Cook---2023---A-Geometric-Framework-for-Odor-Representation.pdf-2-0.png)

MT MT MT


Figure 1: Circuit diagram of the mammalian olfactory bulb. The axons of primary olfactory
sensory neurons expressing the same odorant receptor type converge together as they cross into
the brain and arborize together to form glomeruli (shaded ovals) across the surface of the olfactory bulb. Several classes of olfactory bulb neuron innervate each glomerulus, including external
tufted cells (ET), olfactory nerve-driven periglomerular cells (PGo), and external tufted cell-driven
periglomerular cells (PGe). Superficial short-axon cells (sSA) project broadly and laterally within
the deep glomerular layer, interacting with glomerular interneurons and mediating global feedback inhibition [14]. Principal neurons (MT) include mitral cells and projecting tufted cells, which
interact with the dendrites of inhibitory granule cells (Gr) via reciprocal connections in the external plexiform layer (EPL), and project to several regions of the brain. (Specifically, projecting
tufted cells receive similar afferent input and interact with granule cells as do mitral cells, though
their physiological responses and extrabulbar projection patterns differ [52]. Whereas this geometric framework may apply comparably to both cell types, we refer herein to mitral cells for
simplicity). EPL interneurons and the multiple classes of deep short-axon cell are not depicted.
OE, olfactory epithelium (in the nasal cavity); GL, glomerular layer; MCL, mitral cell layer; IPL,
internal plexiform layer; GCL, granule cell layer. Filled triangles denote excitatory synapses; open
circles denote inhibitory synapses. Adapted from [2].

3


-----

by generalization gradients [37, 55, 58] or by ratings on continuous scales by test subjects

[59]. Indeed, study of the transformations between physical and perceptual metric spaces
is foundational to understanding sensory systems from this perspective [53, 60, 61]. In
contrast, hierarchical structures arise from perceptual categorization processes, though
relationships among the resulting categories still may correlate with underlying similarities in the physical properties of stimuli. Critically, it is categories that are generally
considered to be embedded with associative meaning (categorical perception) [62–65]. Consequently, a useful theoretical framework for olfactory perception must consider the construction of these categorical representations with respect to the physical similarity spaces
that are sampled during sensory activity. That is, along their representational cascades,
olfactory sensory systems can be effectively considered to transition from a physical similarity space metric to a modified perceptual space, within which hierarchical category
representations, generally corresponding to ecologically relevant odor sources, can be
constructed.
Interestingly, the olfactory modality lacks a clear, organism-independent physical metric such as wavelength or frequency along which the receptive fields of different sensory
neuron populations can be deployed (and against which the nonuniform sampling properties of the sensory system can be measured) [1, 2]. However, olfaction does provide
an objective basis for an organism-dependent physical similarity space. In this framework,
the activity of each odorant receptor (OR) type – e.g., each of the ∼400 different ORs of
the human nose or the >1100 different ORs of the rodent nose – comprises a distinct unit
dimension. Specifically, the instantaneous activation level of the convergent population
of primary sensory neurons expressing each OR type [2, 66] provides a value from zero
to one (maximum activation), such that any possible olfactory stimulus can be mapped to
a vector embedded in a physical metric space with dimensionality equal to the number
of OR types. We refer to this receptor activation-based metric space as R-space [29] (Fig.
2A), within which individual vectors directly correspond to physiological measurements
of olfactory sensory neuron activity (e.g., optical recordings from sensory neuron axonal
arbors in the olfactory bulb glomerular layer [15, 16, 67]) and within-category variance is
incorporated into the definition of a learned odor. Critically, in this framework, (1) the
dimensions of R-space are linearly independent of one another, and (2) every possible instantaneous profile of OR activation, including any occluding effects of multiple agonists
and antagonists competing for common receptors, is interpretable and maps to a vector
in R. [29].
Linear independence among the dimensions of R-space is important for analytical
purposes, but their orthogonality is irrelevant [68][2]. This is a vital distinction, not least because the orthogonality of OR receptive fields depends on the properties of the chemosensory input space – that is, the chemical environment – and hence cannot be uniquely defined as a property of the olfactory system per se. In principle, each OR type should have
regions of its receptive field that distinguish it from any other single OR type, such that activation of a given OR need not always imply activation of a particular different OR (that

2Specifically, by the Gram-Schmidt process, the collection of linearly independent sets of maximal size
is in correspondence with the collection of orthonormal bases.

4


-----

#### A B C
 d [per]

 dphys

Figure 2: Depictions of olfactory spaces. [A] Three-dimensional R-space containing three odor
source volumes. Each of the odors activates all of the three receptors (axes) depicted, but with
different ratios of activation. [B] One-dimensional depiction of S-space containing two learned
odors, illustrating the relationship between the physical (dphys; distance along abscissa) and perceptual (d[per]; arc length along the surface) measures of similarity between these separately learned
odor representations. Between-category separation renders d[per] _> dphys. The odor representations_
need not be symmetrical, similar in shape to one another, or equivalent in peak height or area under the distension. Their shapes will be directly reflected in perceptual generalization gradients

[13, 37]. [C] Two-dimensional depiction of S-space with learning-based distensions into the third
dimension. The two odor representations depicted are based on two different ratios of activation
of the two receptors (axes) depicted. The odors are physically similar (proximal), but have been
differentiated both by their statistical learning as separate odors (as in panel B) and additionally
by specific interrepresentational discrimination learning (negative distension located specifically
between the two odor representations, further increasing the perceptual difference d[per] between
these odors). In higher-dimensional spaces, two such odor representations can be separated to a
nearly arbitrary degree without affecting similarity relationships among other nearby odor representations. This can lead to violations of the triangle inequality in d[per] (i.e., ACB < AB). Inset.
Top view of the same two odor representations as in panel C. Note that the variances of the two
receptor dimensions of each representation are independent, and not necessarily symmetrical.

is, no two dimensions will be identical)[3]. However, within any given sensory world, as
defined by a finite set of odorant stimuli with established properties and probabilities of
encounter, there will be reliable activity correlations among many pairs of receptor types
that can support substantial dimensionality reduction [69] (see Efficient coding section).
Critically, however, these reduced dimensionalities are not characteristic of the olfactory
system per se at this level, as they are strongly reflective of the statistics of the stimulus set
used and its particular interactions with the deployed complement of receptors.
Similar dimensionality-reduction efforts also have been applied to olfactory perceptual data [70–72]. These results also are substantially determined by the particular sets of
stimuli employed, but additionally engage the problem of just what the olfactory system
constructs from the space of its underlying physical inputs. It is reasonably clear (even
axiomatic) that the sampling of physical odorant spaces is highly nonuniform [70, 71] –
that is, odor samples are signal sparse [73] – but, perhaps more importantly, the process

3If we think of receptors as functions, then this is saying that the collection of receptors separates points.

5


![](Cook---2023---A-Geometric-Framework-for-Odor-Representation.pdf-4-0.png)

![](Cook---2023---A-Geometric-Framework-for-Odor-Representation.pdf-4-1.png)

-----

of perceptual learning itself directly affects perceived odor similarity relationships, as can
be measured with generalization gradients [13, 37, 74–76]. A general framework for olfactory perception must reflect all of these phenomena, embedding physical and perceptual
similarity spaces into a common geometric framework that admits the construction of
experience-dependent perceptual categories.

###### The geometries of olfaction

In addition to dimensionality, the second fundamental property of a sensory space is its
intrinsic geometry [53]. Establishing a geometry provides access to theorems by which
representational structures can be formally defined and manipulated. However, it is not
necessary to restrict the topology of a sensory space to a single geometry with fixed curvature – in fact, as indicated below, this is neither advisable nor ultimately possible for the
olfactory modality. Specifically, we show that a mature olfactory perceptual space cannot
be simply characterized as ”Euclidean”, ”spherical”, ”hyperbolic”, or otherwise, as its
dependence on localized, experience-dependent plasticity instead produces a space comprising locally modifiable regions that can exhibit the properties of different geometries.
These can be glued together formally via the theory of sheaves.
We present a generalized geometric framework for the construction of odor representations. The framework is based on the molecular/physiological encoding capacities of
the olfactory bulb input layer [29] and the transformation of these physiological odorant
representations by perceptual learning into cognitive, categorical odor representations to
which meaning can be ascribed. Key features of this framework include the simultaneous
depiction of sampling-based physical similarity and learning-dependent perceptual similarity within the perceptual space, and a categorization process that culminates in a perceptual space within which qualitatively discrete odor representations are hierarchically
constructed through experience, exhibiting statistically appropriate consequential regions
with probabilistic boundaries that reflect learned generalization gradients [13, 37, 55, 65].
Critically, individual training and experience generates progressively more sophisticated
hierarchies and concomitantly superior odor identification capabilities [36, 77].
A simplified illustration of the analytical framework is depicted in Diagram 1. Briefly,
the space of instantaneous physical inputs to an olfactory receptor activation space (Rspace) comprising N receptor types can be depicted as an N-dimensional unit cube (Fig.
2A). Transformations arising from initial glomerular-layer computations [2] generate a
modified receptor space termed R[′]; this space inherits the dimensionality of R-space but
respects the nonuniform likelihoods of different state points within that space. The subsequent transformation from R[′] to S-space (”scent space”) reflects the perceptual learning
processes that construct categorical representations of meaningful odors.
This theoretical model does not depend on precisely where in the olfactory representational cascade these transformations occur. However, we consider that the map B
from R-space to R[′]-space reflects signal conditioning computations performed within the
glomerular layer of the olfactory bulb [1, 2], whereas the subsequent transformation into
_S-space is mediated by computations within the olfactory bulb external plexiform layer_
network, inclusive of its reciprocal interactions with deeper olfactory structures (Fig. 1).
Briefly, we propose that the construction of categorical odor representations through sta
6


-----

tistical experience arises from learning-dependent weight changes between mitral cell
principal neurons and granule cell interneurons in the external plexiform layer of the olfactory bulb [28], inclusive of the process of adult neurogenesis, which integrates new
interneurons into the OB circuit via an experience-dependent mechanism and is necessary for odor learning [22–24, 41, 42, 78–80]. The configural receptive fields of granule
cells (as proposed in [2, 28]) provide a high-dimensional state space that enables the representation and storage of statistical priors [81]. To construct this theoretical S-space,
and attribute to it the capacities of generalization and experience-dependent hierarchical
categorization, we first build a transitional space M based on mitral cell activity representations, inclusive of the actions performed on these representations via their interactions
with granule cell interneurons:


_B_

_R_ _R[′]_

_ξ_
∆


(1)


_S_ _M_

_h_

with h ∈ _C[∞](R[m])._
Formally, R is a unit parallelepiped defined by primary olfactory receptor activation
levels. R[′] denotes a subspace of normalized points, following the transformation of sensory input by glomerular-layer circuitry, and is the image B(R). M is a vector bundle
over R[′] of rank equal to the number of mitral cells (Fig. 1) and is generated by mitral
cell output. ξ denotes the input presented to mitral cells following glomerular processing, comprising a sparsened, statistically conservative manifold [82]; it is a section of the
vector bundle M. S denotes the perceptual space, and is realized as a transformation
∆ of R[′]-space that embeds odor learning via smooth functions. This resulting S-space
does not, indeed cannot, admit a single geometry, because of the essential requirement
for locally adaptable curvature. We describe this generative process in detail below.

###### R-Space

The first representational space in olfaction is directly derived from the ligands of the
physical odorant stimulus interacting with the set of chemoreceptive fields presented by
the animal’s primary odorant receptor complement [29]. Both vertebrate and arthropod
olfactory systems are based on large numbers of receptor neurons, each of which expresses one primary odorant receptor out of a family of tens (in Drosophila) to over 1000
(in mice, rats, and dogs). The axons of primary sensory neurons expressing the same receptor converge together to form discrete glomeruli across the surface of the olfactory bulb
(in vertebrates; the arthropod analogue is the antennal lobe), enabling second-order principal neurons (e.g., mitral cells) to sample selectively from one or a few receptor types (depending on species; see M-Space section). The response of each receptor type to an odor
stimulus constitutes a unit vector that can range in magnitude from nonresponsive (0) to
maximally activated (i.e., receptor saturated with agonist; 1). A complete representational
space for instantaneous samples of this input stream consequently has a dimensionality

7


-----

equal to the number of odorant receptor types N. That is, in a species with three odorant
receptors, the space containing all possible instantaneous input signals would be a threedimensional unit parallelepiped (Fig. 2A), whereas the R-space of a mouse expressing
1100 receptor types would comprise a 1100-dimensional unit parallelepiped. Notably,
odorant representations in R-space can be directly measured via optical recordings of activity in the receptor neuron axonal arbors of olfactory bulb glomeruli [15, 16, 67], though
to specify an odorant vector completely would require activity measurements from every
glomerulus. Because the vector coordinate in each dimension depends on the activation
of a qualitatively distinct odorant receptor type, the dimensions can be considered independent of one another. For this, as noted above, it is not necessary that the receptive
fields of the different ORs be orthogonal under all conditions, only that they be linearly
independent [68]; indeed, the orthogonality of their response vectors cannot even be defined without reference to the statistics of the particular physical environment in which
they are deployed.
Formally, R-space is defined as the space of linear combinations of these vectors with
coefficients in (0, 1). Consider the space of all possible odorant stimuli in a species expressing N odorant receptor classes. Each odorant stimulus s[∗] corresponds to a unique
instantaneous glomerular response profile that can be represented as a vector s[∗] _∈_ **R[N].**
Normalizing the activation in each glomerulus enables us to consider s[∗] _∈_ ∏[n](0, 1), the
unit cube in N dimensions. Denote this receptor activation-based representational space
_R. As R is open in the ambient space R[N], R also has dimension N as a manifold._
By considering a product of spaces, we are assuming that the responses of different
glomeruli are orthogonal. In the greatest generality, we would need to consider points
on a unit parallelepiped generated by the primary receptors. That said, we can apply an
invertible linear transformation (specifically, the matrix generated by the Gram-Schmidt
process [68]) to this parallelepiped to generate a cube – a mathematical formalism that
does not affect the particulars of this situation. Consequently, for the remaining sections,
we can assume without a loss of generality that R = ∏[n](0, 1).

###### Glomerular-layer computations, R[′]

The first computational layer of the olfactory bulb – the glomerular layer – computes a
number of transformations important for the integrity and utility of odor representations,
including contrast enhancement [4], global normalization underlying concentration tolerance [13, 14], and potentially other effects [2]. These processes substantially alter the
respective probabilities of the points in R-space. For example, global feedback normalization in the deep glomerular layer [14] ensures that points at which most or all of the
vectors have very high values will be improbable. The outcome of this transformation is
represented as R[′], essentially a smooth manifold embedded in R-space.
In addition to the systematically unlikely points in R that are omitted from the manifold R[′], it is also the case that, under natural circumstances, most of the possible sensory
stimuli s[∗] that could be encountered in R[′] actually never will be encountered in an organism’s lifetime. That is, odor representations within R-space are signal sparse [73]. Moreover, we argue that odor sources s[∗] are discrete, but inclusive of characteristic variance in
quality, and hence constitute volumes (manifolds) within R[′]. To account for this, we de
8


-----

note this variance by s[∗] = (x, Ux), where x ∈ _R[′]_ and Ux denotes an n-tuple of variances
(i.e., one variance for each dimension of freedom in R[′]). That is to say,

_Ux = (σ1[2][, ...,][ σ]n[2][)]_

From this we arrive at the following definition:

**Definition 1.1. A pair (x, Ux) constitutes an odor source volume in R[′]** if Ux is a non-empty
simply connected neighborhood of x and (x, Ux) = s[∗] for some odorant s[∗].

That is, an odor source volume corresponds to a manifold within R[′] that comprises the
population of odorant stimulus vectors arising from the range of variance in receptor activation patterns exhibited by a particular, potentially meaningful, odor source (Fig. 2A)
– here defining source as the odor of some thing (i.e., the sign-vehicle [83]), as opposed to
the thing that smells (the sign-object). This includes variance arising from nonlinearities
in concentration tolerance mechanisms that cannot be fully avoided [13] as well as genuine quality variance across different examples of a source. (For example, the odors of
_oranges vary across cultivars and degrees of ripeness; the odors of red wines vary across_
grape cultivars, terroir, and production methods). The source volume in R[′] thereby corresponds to an odor source (e.g., orange, red wine), inclusive of its variance, and delineates
the consequential region of the corresponding odor category that will be developed via
perceptual learning. Critically, it is not important at this stage to specify multiple levels
of organization within odor sources (e.g., red wine, resolved into Malbec, Cabernet, Montepulciano, etc., then resolved further by producer and season); it is the process of odor
learning itself that will progressively construct this hierarchy of representations at a level
of sophistication corresponding to individual training and experience.

###### M-Space

The transformation from R[′] to S-space depicted in Diagram 1 is mediated by the interactions of mitral and granule cells. In this framework, mitral cells directly inherit afferent
glomerular activity from R[′] (Diagram 1, ξ), but their activity also is modified substantially
by patterns of granule cell inhibition that, via experience-dependent plasticity, effectively
modify mitral cell receptive fields to also incorporate higher-order statistical dependencies sourced from the entire multiglomerular field. (A simplified computational implementation of this constructive plasticity is presented in the learning rules of [28]). This is
depicted in Diagram 1 as an effect C[∞](R[m]) of a mitral cell product space M which contributes to the construction of S, in order to highlight the smooth deformations of R[′] into
_S via passage to M._
These effects of mitral cell interactions, arising from experience, are modeled locally
as a product space M based on the principle that each glomerulus – corresponding to
a receptor type in R[′] – directly contributes to the activity of some number of distinct
mitral cells. In the mammalian architecture, mitral cells receive direct afferent input from
only a single glomerulus, such that the afferent activation of each mitral cell (or group
of sibling mitral cells) corresponds directly to a single receptor type. In this special case,
_M-space is globally a product. To formalize this, we label the glomeruli g1, ..., gq. To each_

9


-----

glomerulus, we associate the number of mitral cells that sample from it; denoted mi ∈ **Z.**
Let k = ∑[q] _mi. Then, the naive space constructed from these data is_

_R[′]_ _× R[k]_ = {(r, v) : r ∈ _R[′], v ∈_ **R[k]}**

The interpretation of this space is as follows. To each point in R[′], we can associate a vector that is an identifier for how subsequent mitral-granule cell interactions in the olfactory
bulb will transform the input in service to identifying it as a known percept. The manifolds associated with particular odor source volumes in R[′] will, owing to experiencedependent plasticity, come to exhibit related vectors that, in concert, manifest sourceassociated consequential regions [55]. These regions reflect categorical perceptual representations [65] and are measurable as olfactory generalization gradients [37, 76]. That is,
the learning-dependent plasticity of synaptic interactions in the OB underlies the creation
of categorical odor representations and manages between-category perceptual separation.
Simplified computational implementations have depicted these acquired representations
as fixed-point attractors, tolerant of background interference and sampling error but lacking explicit consequential regions [28].
_M is always globally a product space (as R[′]_ is contractible). For the mammalian architecture, the dimensionality m of mitral cell output (grouping sibling mitral cells together)
is identical to that of glomerular output k. In nonmammalian tetrapods, in contrast, individual mitral cells may sample from more than one glomerulus [84, 85]. This introduces
a reduction (in general) of the product space such that m now can be less than k. In the
general case where m ≤ _k, the mitral cell space becomes a real rank m vector bundle_

**R[m]** _�→_ _M_ _→[π]_ _R[′]_

over R[′]. In the mammalian architecture, because m = k,

_M = R[′]_ _× R[m]_

thus rendering M a smooth manifold with the convenient property that to every input
_x ∈_ _R[′]_ we associate a point (x, v), where v is a vector whose i[th] component is the value of
the output of the i[th] mitral cell.
Formally, M is a (trivial) vector bundle over R[′] with fibre R[m]. Then, the smooth maps
that send x �→ (x, v), such that composition with projection onto R[′] is the identity, are
called global smooth sections of the bundle, and the set of these is denoted Γ(R[′], M). To
any smooth manifold P, we can associate a sheaf (of rings) of smooth functions

_C[∞](P) = { f : P →_ **R : f is smooth}**

To any open subset, we have a restriction map ResU[P] [:][ C][∞][(][P][)][ →] _[C][∞][(][U][)][. In general, if]_
_U ⊆_ _P is open, then Γ(U, E) is a C[∞](U)−module for any bundle π : E →_ _P. C[∞](−)_
makes P into a locally ringed space and Γ(−, E) is a sheaf of C[∞](−)-modules. These
two sheaves, C[∞](P) and Γ(−, E), fully characterize all of the properties of the manifold
and vector bundle, and, critically, enable the geometric representation of localized synaptic
_plasticity by establishing an algebraic interpretation of local information that can be combined_

10


-----

_formally into global information. (The theory of sheaves is described in more detail below)._
Precisely, to any open cover {Ui} of R[′] and a collection of elements si ∈ _C[∞](Ui) such that_
_si|Ui∩Uj = sj|Ui∩Uj for all i, j there exists a unique global lift s ∈_ _C[∞](R[′]) such that s|Ui = si._
By this method, locally-defined information arising from synaptic plasticity can be glued
together into a coherent whole.[4]

###### S-Space

_S-space, or scent space, is a constructed perceptual space tasked with preserving physical_
similarity relationships among odorants while also embedding the transformations arising from perceptual learning, specifically including those forming incipient categorical
_odors. To do this, we embed R[′]_ into a higher-dimensional space S (with dimension N + 1).
Under this embedding, we represent perceptual learning in S by growing Ux in the positive N + 1th direction around odor source volumes in R[′]. (Discrimination training also
can grow Ux in the negative N + 1th direction, as discussed below). This transformation
does not affect distance relationships in R[N], but systematically increases them in R[N][+][1],
reflecting the process of between-category separation [63, 86]. To quantify this transformation, we construct two distance metrics, dphys and d[per], on S (Fig. 2B).

**Definition 1.2. Let x, y ∈** _S be two points. We define the physical metric between the two_
points as the Euclidean distance between them in R. In notation,

_dphys(x, y) = |πRN_ (x) − _πRN_ (y)|

This metric reflects the physical similarities between odorants in the receptor space, as
defined by commonalities in receptor activation profiles, and which are not affected by
perceptual learning.

**Definition 1.3. Let x, y ∈** _S. Consider x and y as vectors in R[N][+][1]. Then, let γ : [0, 1] →_ _S_
be the curve defined by γ(0) = x, γ(1) = y and πRN (γ[′](t)) = w · [πRN (γ(1)) − _πRN_ (γ(0))]
with w some real number dependent on t. The perceptual metric,

� 1
_d[per](x, y) =_

0 _[||][γ][′][(][t][)][||][dt]_

4This presents the question: what mathematically distinguishes these mammalian and nonmammalian
architectures if their geometry and topology are essentially equivalent? One answer is as follows. In the
mammalian architecture, every odorant induces m distinct functions f1, ..., fm that depend only on a single
coordinate of the input odorant and yield the coordinates of the corresponding mitral cell activation level,
essentially rendering them as maps fi : R → **R. That is to say, tracing an odorant x = (x1, ..., xN) through**
the diagram says that we associate to it a pair (x, v) where

_v = [ f1(x1), ..., fm1_ (x1), fm1+1(x2), ..., fm1+m2 (x2), ..., fm(xN)][T]

In contrast, in the non-mammalian case, the functions generated by sensory input depend on more than
one input coordinate. By labeling the mitral cells using the integers 1, ..., m and setting

_e(i) := {# of distinct glomerular inputs}_

these functions become maps fi : R[e][(][i][)] _→_ **R. While the mappings are foundationally similar, this difference**
renders the latter maps more complicated to analyze.

11


-----

is the arc-length along the surface of S between the points x and y, and reflects the acquired semantic similarities and differences among odors [87] (Fig. 2B). Note that πRN (γ[′])
is well defined as S �→ **R[N][+][1]** and thus the tangent space Tγ(t)S ⊆ _Tγ(t)R[N][+][1]_ = R[N][+][1].

The relationship between these two metrics tracks the changes in S induced by the construction of odor representations; specifically, d[per] reflects experience-dependent changes
in the perceptual distance between x, y ∈ _S that are excluded from the dphys metric (Fig._
2B). Learning about an odor source (x, Ux) progressively distends the volume (in R[N])
in the N + 1th direction, such that the shape of this distension gradually will come to
reflect the odor source volume in R[′]. That is, over time, the breadths (in each of the N
dimensions) of the distension into the additional (N + 1th) dimension will come to reflect
the actual variances Ux of the odor source s[∗] = (x, Ux) as naturally encountered [13].
The quasi-discrete distensions formed in the N + 1th dimension correspond to incipient
categories – i.e., categorically perceived odors – and their breadths and gradients can be
measured behaviorally as generalization gradients [13, 37]. Importantly, the variance for
each dimension of freedom of Ux = (σ1[2][, ...,][ σ]n[2][)][ in][ R][′][ is independent; that is, different sam-]
ples of a given natural odor source may vary substantially in some aspects of quality but
not others, where an aspect of quality refers to the relative levels of activation of a given
odorant receptor type (Fig. 2C).
Formally, to construct the perceptual space S such that there exists a perceptual metric
_d[per]_ that interacts with the natural physical metric dphys of R[′], we consider the embedding
_R[′]_ _�→_ **R[N][+][1]. The open neighborhoods for each odor source volume define open sets in**
the subspace topology. If we embed R[′] by the canonical inclusion R[N] _→_ **R[N][+][1], then R[′]** is
flat in R[N][+][1] because the final coordinate of its elements is 0. Therefore, we can consider
transformations of R[′] that smoothly vary the final coordinate. For each transformation f,
denote the resulting space as S := S( f ); this constitutes the evolving perceptual space.
Define the map ∆ : R[′] _→_ _S as the distension of R[′]_ in N + 1 (Diagram 1). This map arises
from considering M and R[′] simultaneously, and is a diffeomorphism trivially.
To better understand the map ∆, we here construct it as the composition of maps
among the spaces already described, specifically showing how the (acquired) properties
of M govern the mapping of R[′] to S. The map B : R → _R[′]_ reflects glomerular-layer transformations as described above. For a fixed smooth section ξ : R[′] _→_ _M (which always_
exists by the triviality of M), we generate Diagram 2 (an elaboration of Diagram 1),


_B_

_R_ _R[′]_

_ξ_
∆( f )


(2)


_S_ _M_

idR′ _× f_

where ∆( f ) is defined to be a map that makes the diagram commute.

**Definition 1.4. Let (x, Ux) be an odor source volume in R[′]. We denote the image of this**
volume in S as (x, _U[�]x). This image denotes an odor representation, also referred to simply_
as an odor.

12


-----

###### The theory of sheaves enables a geometric framework based on local plasticity

Plasticity in neural systems in general, and in the olfactory bulb in particular, is locally
governed. Changes in cellular and synaptic properties rely on the interactions of directly
connected neurons and the locally regulated release of neurochemicals. These local effects, coordinated by sophisticated circuit interactions, collectively generate global performance at the network level. For example, in the olfactory bulb, the activity of mitral
cells is shaped by local inhibition delivered by granule cells (Fig. 1). The action of a particular granule cell upon a particular mitral cell is uniquely determined via local synaptic plasticity, and it is this very uniqueness of each individual granule-to-mitral action
that determines (collectively) the global transformation underlying perceptual learning.
However, while these local distortions transform the perceptual space (via distensions in
_S), they are neither globally governed nor constrained by the original geometry of the_
global system. To formally glue these many local plasticity operations, together with any
relevant global processes, into a single analytical framework, we employ the theory of
sheaves [88] (Fig. 3).
Briefly, we can consider olfactory bulb plasticity to modify local functions from M −
_space to S −_ _space. Because this plasticity affects local neighborhoods consistently, the_
overlaps between these neighborhoods will agree, and then the collection of functions
from M to S will form a sheaf. That is, the theory of sheaves enables us to glue all of these
local functions together into a unique global function M → _S. A more formal description_
follows.

**Definition 1.5. A presheaf on a topological space X with values in Set is a functor F :**
Open(X)[op] _→_ **Set. A sheaf is a presheaf that satisfies the additional conditions:**

(Sep) If {Ui} is an open cover of an open set U, and there exist s, t ∈ _F(U) such that_
_s|Ui = t|Ui for all i, then s = t._

(Sh) If {Ui} is an open cover of an open set U, and there exists fi ∈ _F(Ui) for all i such that_
_fi|Ui∩Uj = fj|Ui∩Uj for all pairs (i, j) then there exists f ∈_ _F(U) such that f |Ui = fi._

Presheaves satisfying the first property are referred to as separated (the separation axiom implies that the second property yields unique lifting). To illustrate, consider the
square blue section π[−][1](Uα) of the M¨obius band in Figure 3. By covering the arc of
the circle corresponding to this section (Uα) with small segments Ui (which correspond
to vertical bars π[−][1](Ui) on the M¨obius band in the same way as the segment p corresponds to the bar π[−][1](p)), we then can consider continuous functions from the arc of
small segments back into the square. We denote this collection of functions Γ(U, M). Corresponding to the open cover, we can consider and modify different collections Γ(Ui, M)
that are nonoverlapping subsets of Γ(U, M). We then pick functions fi on each Ui such
that they agree on the overlap of the sets. We then know we can construct a function
_f : Uα →_ _Uα × R which restricts correctly. In this example case, the functions are simple,_
so the use of sheaves contributes little utility; however, when working with values that
are more arbitrarily determined, sheaves enable them to be treated as a geometric whole.

13


-----

_π[−][1](p)_


_π[−][1](Uα)_

_α_

###### Uα × R


Figure 3: Illustration of the theory of sheaves. The figure depicts a non-trivial vector bundle
(a M¨obius band) over the circle. The projection map π sends points on the M¨obius band to the
corresponding point on the central circle. We therefore can pick coordinates on the M¨obius band
such that, for each point p in the circle, there is a line π[−][1](p) (the preimage, red) in the band. The
map φα is a local trivialization of the bundle on the open set Uα, showing how the M¨obius strip is
locally ”flat” (whereas globally it is not). To obtain a sheaf from this picture, we consider the set of
all possible embeddings of the circle (or segments thereof) into the M¨obius band. This will assign
to a segment (such as Uα) the collection of all such embeddings of this segment into Uα × R. In
this sense we think of the M¨obius band not as its own space, but instead as a collection of lines
glued together in a particular way. This set of embeddings is a prototypical example of a sheaf.
[Modified from Figure 18 in [89] using code adapted from http://theoreticalphysics.info.](http://theoreticalphysics.info)

Indeed, sheaves can be considered generalizations of the M¨obius band (a vector bundle)
in that the stalks/fibres π[−][1](p) are no longer required to be uniform.
Formally, we consider the local actions of granule cells onto mitral cells, and their
concomitant modification of mitral cell output, as follows, considering that these actions
may rely both on afferent sensory information and on additional inputs delivered onto
granule cells from other sources such as piriform cortex [20, 21]. Recall from the previous
section that for any smooth vector bundle π : E → _P, we get two sheaves C[∞](−) and_
Γ(−, E) on P such that Γ(U, E) comes equipped with an action of C[∞](U) for all open U ⊆
_P. We here formally define an analogous pairing of sheaves to describe the modification_
by granule cells of afferent information contained in the mitral cell ensemble.
The first step in this formal definition is to define a functor

_µ : T →_ **R[m]**

where T is the category defined by the topology on R[′], and R[m] is the category whose
objects are linear subspaces of R[m] and the morphisms


MorR[m](U, V) =


�
∅ _U ̸⊆_ _V_
_{∗}_ _U ⊆_ _V_


14


-----

**Lemma 1.6. For any subspace U ⊆** **R[m], define a sieve S on U by a family of subspaces V ⊆** _U_
_such that if V[′]_ _⊆_ _V ∈S then V[′]_ _∈S. Set J(U) to be the collection of all such sieves on U. Then,_
_by this notion of sieve, (R[m], J) defines a site (that is, J defines a Grothendieck topology)._

_Proof. This lemma follows immediately from the proof that the category T with the stan-_
dard notion of covering is a site. For such a proof, see [90, Chapter III].

Importantly, odorant presentations do not excite all receptor types, and therefore will
activate some, but not all, mitral cells. This corresponds to the situation where ξ(s) =
(s, v) and v has some coordinates equal to 0. The non-zero coordinates form a basis for
some subspace of R[m]. Let n(ξ, s) be the number of non-zero coordinates in v. Let O be
any open subset of R[′]. Then
_µ(O) = R[ℓ]_

where ℓ = max{n(ξ, p) : p ∈ _O}. This construction shows that µ is functorial._

**Lemma 1.7. Let F be a sheaf on R[m]. Then, the functor µ[∗]F** (−) := F (µ(−)) ∈ **_Sh(R[′])._**

_Proof. The fact that this is a presheaf is immediate; thus it suffices to show that the gluing_
condition is satisfied. Let U ⊆ _R[′]_ be an open set and {Ui}i∈I an open cover of U. Suppose

further that we are given fi ∈ _µ[∗]F_ (Ui) for each i so that Res[U]U[i]i∩Uj _[f][i][ =][ Res]UUij∩Uj_ _[f][j][. We]_

want to show that there exists some f ∈ _µ[∗]F_ (U) such that Res[U]Ui _[f][ =][ f][i][. As][ {][U][i][}][ is an]_
open cover of U, {µ(Ui)} will form a covering for µ(U) in the sense of a Grothendieck
topology. Combining this with the fact that F is a sheaf on R[m] implies that there exists a
unique f ∈ _µ[∗]F_ (U) satisfying the condition above. Hence, µ[∗]F ∈ **Sh(R[′]).**

**Lemma 1.8. By abuse of notation, C[∞]** _is a sheaf on R[m]._

_Proof. The canonical functor jX : Open(X) →_ **Top (which sends each open set U ⊂** _X to_
itself treated as a topological space and the inclusions iU : U → _X sent to the associated_
embeddings) induces a functor between the presheaf categories

_jX[∗]_ [:][ Set][Top][op][ →] **[Set][Open][(][X][)][op]**

given concretely by
_jX[∗]_ _[F]_ [(][U][)][ :][=][ F] [(][U][)][.]

Therefore, it follows that a presheaf on a category of topological spaces is a sheaf if and
only if it is a sheaf on each topological space. As C[∞] is a sheaf on each R[ℓ], it follows that
_C[∞]_ (by abuse of notation) is a sheaf on R[m].

**Corollary 1.9. µ[∗]C[∞]** _∈_ **Sh(R[′]).**

All of this together provides a mathematical formalism for learning local data in R[′].
We begin with a (small) open neighborhood of an odor (x, Ux). Applying µ[∗]C[∞] we obtain
the mitral cells with non-zero activation on points in this open set (and hence for all points
in Ux) and the collection of all smooth functions on their output (the particular R[ℓ]). The
choice of a particular smooth function is then quantifying a local change in S. Now, we

15


-----

define G(−) as a flabby (flasque) sheaf of rings on R[′] which act on µ[∗]C[∞]. This action
performed by the sheaf G is precisely the delivery of local inhibition onto mitral cells,
and in particular to those mitral cells that are activated by a given odorant stimulus. This
corresponds to the process by which activated receptors (fibers over the open set of the
odor stimulus that are nonzero) propagate activity through the network based on the
existing synaptic graph, and thereby induce plasticity according to local rules, without
any need to globally update a learning map.
With the definitions of R, R[′], M, S, and G, we now can generate a fully explicit depiction of the model introduced in Diagram 1. Using the theory of sheaves, we glue the local
inhibitory actions encoded in sheaf G into a global action, µ[∗]C[∞], that embodies the localto-global transformations of these granule cell actions and enables their interaction with
the global mapping of M → _S that preserves R[′]. Together, these underlie the concerted_
global transformation of the perceptual space – i.e., the construction of S.


_R_ _B_ (R[′], G, µ[∗]C[∞])

_ξ_
∆(g)


(3)


_S_ _M = R[′]_ _× R[m]_

IdR′ _×g_

Formally, this diagram encompasses a commuting diagram of smooth manifolds. As
we are considering sheaves on R[′], all of these maps are indeed morphisms of ringed
spaces. Newly associated with the space R[′] are G, a sheaf constituting the granule cell
modifications to perceptual output (which embeds the organism’s prior learning), and
the G-module µ[∗]C[∞], a sheaf of modules over each set of sections. As with Diagrams 1 and
2, we can track the path of a single odorant stimulus (a point in R) through the diagram
until is it realized as a perceptual quality (a point in S). Specifically, an individual odorant
is sent from R to R[′] via the map B, a set of signal conditioning transformations performed
by glomerular-layer circuitry. ξ then represents a particular choice of section of the vector
bundle M which immerses R[′] into M. This explicitly realizes the associations between
glomeruli and mitral cells. The final morphism IdR′ ×g represents the building of the
perceptual space. In total, (IdR′ ×g) ◦ _ξ is a diffeomorphism of R[′]_ to S in such a way that
the modifications arising from perceptual learning are realized as increased heights in the
final coordinates of points in the N + 1th dimension of S. The summary ∆(g), then, is
simply the induced map by the composition.
In sum, Diagram 3 illustrates how the theory of sheaves enables the formal representation of idiosyncratic, experience-dependent, locally-governed transformations of olfactory perceptual space within a global geometric framework. Odor learning generates
locally-determined curvature within S-space, mapped as distensions into the N + 1 dimension – a transformation that has has several critical consequences. First, these plastic
changes underlie a process of category learning based upon the profiles of these quasidiscrete distensions, which correspond to potentially meaningful odor sources, reflecting
the environmental reality that odor sources of interest are generally discrete but inclusive
of natural variance. Second, the preservation of physical similarity information within
and among categories preserves a broad capacity to revise or elaborate learned categories,
or even to remap similarity relationships based on new experience. Third, as a necessary

16


-----

consequence of local plasticity, geometric frameworks for olfaction that are based on fixed
curvature, whether it be Euclidean, hyperbolic, or otherwise, are unambiguously ruled
out.

###### Dynamics of odor category learning

In the present framework, the process of odor learning generates a distension into the N +
1 dimension of S that reflects the odor source being learned, inclusive of variance. This
distension is an incipient category, and can be mapped back to an odor source volume
in R (Fig. 2A). Olfactory perceptual learning studies suggest that such distensions are
initially broad across N dimensions, but with accumulated experience come to reflect
the actual N-dimensional quality variance profile exhibited by the natural odor source

[13, 37, 91]. The learned variances associated with each dimension of R are presumed to
be independent (receptor-specific), and the generalization gradients observed along any
arbitrary trajectory through R reflect the degree of distension into N + 1 exhibited at each
measured point along that trajectory.
Critically, all of these transformations have timescales. Learning takes time, and experiences that are rare, weakly attended, and/or of little consequence are not retained
for long. It is well established that fear memory persistence in the hippocampus depends strongly on the intensity of reinforcement, mediated by specific signaling pathways [92, 93]; similar mechanisms for memory regulation have been identified throughout the brain [94, 95], including within olfactory bulb [38]. For example, in olfactory
habituation and spontaneous discrimination studies, in which odors are presented without an associated contingency, rodents’ memory for these odors persists only on the order of minutes [96–98]. In contrast, when specific odors cue the availability of reward
(reinforcement learning), odor memory after just 20 massed presentations is maintained
for over two days (this persistence requires intact noradrenergic signaling and protein
synthesis-dependent long-term memory consolidation mechanisms within the olfactory
bulb) [99, 100]. Odors that are experienced as consistently meaningful over extended
periods of time, of course, yield famously persistent memories [101]. Accordingly, the
_S-space landscape should be considered dynamic, with distensions into N + 1 extending_
and often retracting in time according to the diverse underlying timescales of network
plasticity. Over time, however, the S-space of a given individual will develop a persistent
topography in the N + 1 dimension reflecting their accumulated knowledge and experience. Representations of environmental odor sources, such as ”orange”, will be common
to different individuals only by virtue of their shared experience.

###### Discrimination learning

Introducing curvature into S-space is fundamentally a process of unsupervised statistical learning, inclusive of reinforcement and/or other relevant influences. One- or fewtrial learning experiences generate broad generalization gradients [13, 37], the breadths of
which reflect the higher level of uncertainty afforded by undersampling. Consequently,
responses to highly similar odors initially will tend to fall into the same consequential

17


-----

region; that is, the implicit interpretation would be that these odors are examples of
within-category variance. However, this changes when specific discrimination training
paradigms are used. Odor pairs that are not spontaneously distinguished can become
rapidly distinguishable after they are associated with different reinforcers [102]. While it
is possible that discrimination between such similar odors could be achieved by asymptotic levels of statistical learning – a gradual sharpening of their respective S-distensions
into mature forms with reduced overlap – the rapidity of discrimination learning and its
dependence on reinforcement suggests an additional, directed process.
In category learning, perceptual differences arise from increasing the intervening perceptual distance between categories (between-category separation; [86]). Discrimination
training is capable of rapidly and strongly rendering similar odors more perceptually
different from one another than they were prior to learning – that is, of selectively increasing the arc-length distance between their category representations in S. Consequently, to
avoid an arbitrary floor effect constraint, discrimination learning must be able to not only
retract between-category S-distensions to zero, but to extend them in the negative direction when warranted (Fig. 4B). A second difference between discrimination learning and
ordinary statistical learning is that the former is specifically targeted between two or more
categories, rather than transforming the full extent of either individual category (Fig. 2C).
Accordingly, these retractions in S will be localized between the specific categories that
are being discriminated, and furthermore they may be emphasized specifically in those
dimensions of S in which the categories would otherwise overlap. Consequently, in the
higher-dimensional S-spaces typical of biological olfactory systems, such localized retractions between two odors need not generate inappropriate side effects on the pairwise
similarities between other odors. Overall, discrimination learning serves as a prominent
substrate of olfactory expertise, in which trained individuals can easily and reliably recognize subtle distinctions that the untrained may not even perceive.
Formally, consider two physically similar odorants s[∗] = (x, _U[�]x) and t[∗]_ = (y, _U[�]y) in S._
Because the early stages of odor learning are characterized by broadened generalization
gradients [37], reflecting sampling uncertainty, their odor representations (distensions in
_S) at this stage are likely to overlap:_ _Ux ∩_ _U[�]y ̸= ∅. This is appropriate, given the prior_

[�]
likelihood that two highly similar odor stimuli, sampled in close succession, simply constitute two samples from the same odor source volume. To increase the discriminability
of these similar odors, we construct a map that reduces only those values of f which are
sufficiently close (within some small ε > 0) to a distance-minimizing path γ connecting
_x and y. Its existence follows from the existence of smooth bump functions on M. Fix_
_f ∈_ _C[∞](R[m]) so that S = S( f ). We consider functions α ∈_ _C[∞](R). Then, by defining the_
learning operation as S �→ _S(α ◦_ _f ) we have a realization of this transformation by which_

two odor representations are progressively separated by learning. Denoting by _C[�][∞](R)_

the constant sheaf corresponding to C[∞](R) on R[′], we here have defined a _C[�][∞](R)-module_
structure on µ[∗]C[∞]. Therefore, by considering only the interaction of α and f over γ, we
have reduced the problem of discrimination learning to a one-dimensional problem. Accordingly, the map resulting from discrimination learning lengthens the perceptual metric
_d[per]_ between two similar odor source volumes, partitioning and expanding the previously
shared space between the two representations so as to arbitrarily increase their perceptual

18


-----

dissimilarity without altering the physical distance dphys between their centers.

**Remark 1.10. Based on the construction above, we can take** _C[�][∞](R) to be a rough approx-_
imation of G as a sheaf. We cannot conclude that they are precisely equal, as this would
require further analysis that is not presented here.

**Remark 1.11. Retractions in the N + 1 dimension of S owing to discrimination training**
between specific categories can result in violations of the triangle inequality [103] – that is,
discrimination training between odors A and B, but not between either of these and odor
C, could lead to d[per](ACB) < d[per](AB). This is psychophysically correct, but renders
the perceptual metric d[per] not formally a metric. We nevertheless refer herein to d[per] as
a metric for simplicity, and because this technicality does not affect how this measure of
distance is used. Interestingly, this recalls the argument by Tversky [57] that perceptual
similarity, for this very reason, should be modeled using set theory rather than metric
spaces. We address this issue in the Semantic similarity and contrast models section below.

In summary, the process of discrimination training allocates resources to the specific
categorical separation of odor sources that are highly physically similar and yet must be
reliably distinguished. This capacity to learn to perceptually distinguish very similar odor
sources may underlie natural feats such as, for example, the odor-based social recognition
of individual conspecifics [104, 105]. However, this acquisition of expertise is an effortful
process, likely constrained by broader systemic limits on representational capacity, and
hence cannot be casually extrapolated. (Recent claims that humans can distinguish one
trillion odors [106] arise from this error, among other errors previously identified [60,
107]). The development, over an individual’s lifespan, of a richly featured landscape in
_S is diagnostic of that individual’s acquired olfactory expertise – the richest examples_
of which may be found associated with hunter-gatherer subsistence strategies [108] and
with professions such as perfumer, chef, and sommelier.

###### Constructed hierarchical categorization

Experience-dependent plasticity introduces curvature into S, distending and shaping incipient odor source categories and augmenting learned distinctions among them. This
process powerfully reshapes perceptual similarity space, modifying the perceptual distances d[per] among categorical odor representations without altering the physical distance
metric dphys. We refer to the more persistent effects of learned experience as expertise,
and describe how this training enables an expert to easily distinguish subtly different
odors that are perceptually indistinguishable to the untrained. However, experts also remain able to recognize the broader categories; being able to make fine distinctions does
not imply that those distinctions are always appropriate or relevant to the task at hand.
Moreover, the finest distinctions are likely to require correspondingly higher-fidelity information, whether based on a stronger, cleaner signal, the accumulation of certainty over
time, or both. Notably, the olfactory system exhibits a speed-precision tradeoff [109] (often conceived as a speed-accuracy tradeoff owing to the experimental methods used to
measure it), in which more difficult olfactory discriminations require correspondingly

19


-----

more time to resolve [110–114]. All of these circumstances – task-specific generalization,
low-fidelity sampling, and time-constrained decisions based on partial information – require the identification of unambiguous broader equivalence classes. That is, if there is
not enough certainty to identify a particular Walla Walla Cabernet Sauvignon, there may
yet be enough to identify a Cabernet, or simply the scent of wine. In this way, olfactory
categorization can be conceived as hierarchical.
Hierarchical categorical perception [83] is a natural emergent property of S-space curvature. That is, based simply on the cumulative effects of statistical and discrimination
learning, odor categories can admit more specific subcategories to an indefinite degree.
Lifelong experience thereby generates a mature landscape in the N + 1 dimension of
_S-space, with greater olfactory expertise yielding a correspondingly richer, hierarchical_
landscape, studded with complex patterns of peaks, ridges, and valleys. In a depiction of
a mature S-space (Fig. 4), particular points in R map directly onto the finest categorical
resolution constructed by that individual. The speed-precision tradeoff can be depicted
as a gradual, progressive elevation of a sample point along the N + 1 dimension of S,
such that at any given time it may only be possible to identify a broader equivalence class
within which the point is located, even if more time would permit a higher-resolution
classification (Fig. 4A, arrows). Irreducible uncertainty in stimulus sampling can be modeled by a finite surface with dimensionality equal to R[′]; in the one-dimensional example
depicted, this corresponds to a horizontal line segment depicting the resulting sample
uncertainty, which may prevent the resolution of that sample beyond a bifurcation in the
hierarchy, thereby limiting sample identification to a broader equivalence class (Fig. 4C,
_arrow). For example, a sample of wine in the kitchen might be readily identifiable by a_
sommelier as pinot noir, but could only be further resolved by that individual into vintage
and producer in a chemically ’quieter’ environment. In all cases, the number and hierarchical complexity of odor representations in S-space depend on the acquired expertise of
the individual.

###### Semantic similarity and contrast models

In addition to distinct odors being perceived as similar based directly on their proximity in S, judgments of similarity and even odor identification can depend on context and
other situational priors. How can these phenomena arise from a geometric framework
based on the receptor-based physical similarity of R-space? Indeed, for this very reason,
Tversky and colleagues argued that geometric models and hierarchies are not dependable
bases for perceptual similarity. Instead, similarity was defined using a contrast model derived from set theory, in which the similarity of two percepts depended on the number of
features that they shared [57, 103]. (Exactly what counted as a feature for this quantitative
purpose remained undefined). This set-theoretic framework naturally allowed that similarity might depend on context, in that some features might be weighted more strongly
than others and that this weighting might change. Such processes can easily lead to violations of the triangle inequality for objects that differ on two or more separable dimensions
of similarity [103], which traditionally has been interpreted as an argument against geometric models of similarity.

20


-----

**A** Final categorical **B** **C**

classification

Final equivalence class

Equivalence class(es) given limited sampling time _dphys_ _d_ _per_ given sample uncertainty

Odor sample 1 Odor sample 2

Figure 4: Elaborated one-dimensional S-space with distensions into the N + 1 dimension. Three
broad categorical odor representations (A, B, C) are depicted, each admitting multiple narrower
odor representations within the larger category. Odor samples (blue line segments) exhibit a measure of irreducible sample uncertainty in dphys that is denoted by the length of the segment (more
generally, by a finite surface with dimensionality equal to that of R[′]). Odor sampling and recognition is depicted by migrating the odor sample progressively upward in the N + 1 dimension on
a behaviorally relevant timescale (sampling time arrow). During sampling, the internal representation of that odor sample at any given time will be the equivalence class corresponding to that
point in time. Accordingly, the initial representation (lowest horizontal dotted red line in A and C)
will be correspondingly broad, communicating only the identity of the broadest category to the
animal. With ongoing sampling, the non-irreducible uncertainty will be progressively reduced
and the equivalence class will narrow into increasingly specific hierarchical subcategories as the
sample progresses upwards in N + 1 (horizontal dotted red lines). This reflects the olfactory speedprecision tradeoff, in which odorants of greater physical similarity require correspondingly more
time to reliably differentiate, whereas broader classification decisions can be made more rapidly if
time constraints govern performance on a behavioral task [110–112]. Importantly, discrimination
learning increases d[per] specifically between odor representations (dashed curve in B, compare with
_dphys), thereby enabling faster and more reliable discrimination between those representations (see_
also (Figure 2C)). In high dimensional spaces, any two representations generally can be so separated without affecting the perceptual relationships of other neighboring odor representations.
That is, whereas in one dimension, as pictured above, the localized retraction between two specific
odor representations within panel B also alters the perceptual distance between, for example, the
odors depicted in panels A and C, in higher dimensional spaces this side effect would not follow.
Finally, odor samples with irreducible uncertainty that cannot be resolved into a single terminal
hierarchical category can be ultimately classified at a lower hierarchical level (final equivalence class,
C).

In the present geometric framework, however, local plasticity can freely generate violations of the triangle inequality in d[per]. Discrimination learning, for example, can arise
from selectively reducing the weighting of features (ultimately, receptor activities) that
are common to two similar odors, based on the emerging configural recognition of one of
these trained odors. That is, owing to local plasticity and aided by high dimensionality,

21


![](Cook---2023---A-Geometric-Framework-for-Odor-Representation.pdf-20-0.png)

**A** **B**

classification

Final equivalence class

Equivalence class(es) given limited sampling time _dphys_ _d_ _per_ given sample uncertainty

Odor sample 1 Odor sample 2


-----

the present geometrical framework can admit this essentially nonmetric transformation
of similarity relationships. Indeed, the embedding of arbitrary priors (here arising from
experience-dependent local plasticity) in high-dimensional neural systems has been recognized as having properties akin to set theory, in that these priors comprise features that
can be shared among stimuli [81] – recalling existing arguments that the dichotomy of
geometric and contrast models is ultimately immaterial [54]. The retention of geometrical
properties is of course valuable for analysis, as contrast models otherwise admit no clear
basis for representing the physical properties that underlie odor category variance and
demarcation.
The weighting of features also can be influenced by external inputs to the olfactory
bulb. It is well established that ascending inputs from the piriform cortex and other regions of the brain can selectively activate granule cells [20, 21], potentially biasing bulbar
odor representations with top-down priors [28]. In the present framework, such inputs
could transiently alter the geometric properties of the sheaf G (Diagram 3), enabling a
remapping of the similarity relationships among certain learned odor categories. For example, a top-down focus on features of sweetness might increase the similarity of orange
to apple and reduce its similarity to lemon, dynamically modifying d[per] relationships in
order to emphasize or disregard selectively targeted features of dissimilarity. In contrast,
a top-down focus on features of citrus would exert a contrary effect. Representations of
external cues, such as spatial context, also can bias the interpretation of olfactory stimuli [50, 115]. In sum, whereas we propose that experience-dependent transformations
of S-space include persistent physiological changes that instantiate a critical substrate
for long-term odor memory within the circuitry of the olfactory bulb and its immediate targets [38, 99], the process of olfactory perception also admits dynamic, task-specific
mechanisms that likely modulate these circuits substantively.

###### Efficient coding

The intrinsic dimensionality of olfactory encoding has been a topic of contention. In part,
this is a red herring, as dimensionality is not a property of the olfactory system per se,
but rather characterizes particular models of specific aspects or stages of representation.
However, there is an important bifurcation in the set of existing models. The first type
of model is based on the intrinsic high dimensionality of R-space, and focuses on problems of primary stimulus encoding and neural circuit processing motifs (notably, these
can differ substantially from analogous motifs employed in other sensory systems that
operate on lower-dimensional feature spaces [1, 4, 116]). Such models emphasize the
coding potential and corresponding low-level physiological mechanisms of relatively peripheral layers of the olfactory system. In contrast, the second type of model is generally
based on reports of psychophysical similarity, the results of which then are condensed
onto a reduced dimensionality using tools like principal components analysis [70, 72] or
non-negative matrix factorization [71]. These graph-theoretic models eschew questions of
coding potential in favor of depicting the current perceptual relationships among odors
that already have been encoded. The specific dimensionality estimates in these works are
necessarily limited by the scope of the odor sets employed, and certainly are influenced
by the nature of the questions used to obtain the data, but this does not invalidate the

22


-----

basic concept that one can legitimately construct psychophysical spaces of substantially
lower dimensionality than the R- and S-spaces discussed herein. What is the research
value of these descriptive spaces, and how do they relate to the present framework?
The broadest arguments for reduced dimensionality are related to the efficiency of
memory search – i.e., the ability to quickly recognize known stimuli along with perceptually similar variants that may have similar implications. High-dimensional spaces are
vast, and the efficiency of retrieval is paramount for organisms in the wild.[5] Fortunately,
_S-space is highly reducible, because the olfactory modality is signal sparse [73]._ This
sparseness property is not directly related to the proportion of neurons that are active
at any given time; rather, it indicates that, of all the distinguishable states that a neural
system could assume, only a very few are ever actually occupied. That is, within a bewilderingly high-dimensional R-space, the vast majority of that volume corresponds to no
meaningful odor and may never even be experienced in an animal’s lifetime.
An efficient system will adapt to signal sparseness, preferentially allocating resources
to encode the properties of stimuli that actually exist [117, 118]. Current models of bulbar plasticity achieve this by utilizing configural plasticity and the selective allocation of
adult-generated interneurons (adult neurogenesis) to enable lifelong learning capacities
within active, occupied regions of R-space [28, 119]. These regions of stimulus-occupied
space can then, in principle, be selectively projected onto a new basis that is representationally compact and amenable to efficient search. Two classes of transformation that
enable such dimensionality reduction while preserving similarity relationships are those
that enable categorization and those that support regression [54]. The transformations of the
present framework afford the advantages of both of these methods, enabling experiencedependent category formation while preserving a physical basis for intercategory similarity upon which further basis transformations can be performed. For present purposes,
this dual capacity enables the construction of transformed spaces comprised of the category representations of known odors, remapped onto a new basis that excludes unoccupied regions of R-space and may either directly inherit the similarity relationships of d[per]

or modify them owing to additional higher-level inputs. We refer to these transformed
spaces as T-spaces.
Notably, operational T-spaces in this framework must be dynamic. That is, if categorical odor representations are constructed through plasticity, then newly learned representations (or modifications of existing representations that acquire new qualities or d[per]

relationships) must be able to establish themselves within the similarity relationships of
_T-space. Much of the time, this enrichment will require some reconstruction of an existing_
_T-space (potentially including a modest expansion of T-dimensionality), and therefore_
must induce a degree of ongoing remapping of the underlying physical representation
across some postbulbar area(s) such as piriform cortex and olfactory tubercle (aka tubular
striatum [120]). Indeed, odor representations in piriform cortex do appear to exhibit progressive remapping over time [121]. Moreover, such representational drift increasingly
appears to be the rule rather than the exception across the brain [122, 123], being evi
5The problem posed by high dimensionality to memory search efficiency may be overemphasized, because the control-flow methods used by contemporary computer architectures are particularly vulnerable
to the curse of dimensionality. The decentralized architecture and localized computational tactics employed
by brain circuits need not suffer from this curse.

23


-----

dent particularly in visual cortex [124], parietal cortex [125], and hippocampus [126, 127].
Additional factors potentially affecting T-space formation include the merging of contextual information into odor representations, likely even within olfactory bulb [49, 50, 115].
For present purposes, however, T-spaces remain weakly defined. They are not necessary
elements in the present construction, except as an illustration of the theoretical reducibility of S. Indeed, postbulbar ”odor representations” in the brain may be better described
as odor-informed state or goal representations, in which T-spaces are dynamically constructed for cause and necessarily integrative and multimodal.

###### Conclusion

We present a general geometric framework outlining the operation of the vertebrate early
olfactory system and illustrating how category learning underlies the efficient encoding
of environmental odor sources into quasi-discrete, meaningful odors and underlies the development of olfactory expertise. The construction of the resulting S-space corresponds to
experience-dependent plasticity within the circuitry of the deep olfactory bulb, inclusive
of its reciprocal interactions with its immediate follower cortices. Because of the heuristic,
statistical, and distributed nature of this plasticity, a single geometry with fixed curvature
does not suffice to describe the system; instead, the theory of sheaves is used to glue
these diverse, localized changes into a coherent geometric whole. The framework unifies
a broad range of experimental results and theory, from the physics of ligand-receptor interactions, to the plasticity of bulbar circuits and the acquired configural receptive fields
of interneurons, to the formation of generalization gradients, the speed-precision tradeoff, and the capacities and predictions of competing cognitive models of similarity. Categorical odor perception is depicted as an ongoing, constructive process of segmentation
arising from deformations of S-space, admitting multiple hierarchical layers within categories and multiple timescales of local plasticity. This framework is sufficiently concrete
to serve as a roadmap for the development of operational brain-inspired artificial systems
capable of rapid prototype learning.

###### Acknowledgments

We gratefully acknowledge Alec J. Mutti and Zarina R. Lagman for assistance with figures, and the members of the Computational Physiology Laboratory for challenging discussions and advice.

24


-----

### References

[1] Cleland, T. A. Construction of odor representations by olfactory bulb microcircuits.
_Prog. Brain Res. 208, 177–203 (2014)._

[2] Cleland, T. A. & Borthakur, A. A systematic framework for olfactory bulb signal
transformations. Frontiers in Computational Neuroscience 14, 85 (2020).

[3] Yokoi, M., Mori, K. & Nakanishi, S. Refinement of odor molecule tuning by dendrodendritic synaptic inhibition in the olfactory bulb. Proc Natl Acad Sci U S A 92,
3371–3375 (1995).

[4] Cleland, T. A. & Sethupathy, P. Non-topographical contrast enhancement in the
olfactory bulb. BMC Neurosci 7, 7 (2006).

[5] Fukunaga, I., Herb, J. T., Kollo, M., Boyden, E. S. & Schaefer, A. T. Independent control of gamma and theta activity by distinct interneuron networks in the olfactory
bulb. Nat Neurosci 17, 1208–1216 (2014).

[6] Werth, J. C., Einhorn, M. & Cleland, T. A. Dynamics of spike time encoding in the
olfactory bulb. BioRxiv doi: 10.1101/2022.06.16.496396 (2022).

[7] Li, G. & Cleland, T. A. A coupled-oscillator model of olfactory bulb gamma oscillations. PLoS Comput. Biol. 13, e1005760 (2017).

[8] Li, G. & Cleland, T. A. A two-layer biophysical model of cholinergic neuromodulation in olfactory bulb. J. Neurosci. 33, 3037–3058 (2013).

[9] Kashiwadani, H., Sasaki, Y. F., Uchida, N. & Mori, K. Synchronized oscillatory
discharges of mitral/tufted cells with different molecular receptive ranges in the
rabbit olfactory bulb. J. Neurophysiol. 82, 1786–1792 (1999).

[10] Bathellier, B., Lagier, S., Faure, P. & Lledo, P. M. Circuit properties generating
gamma oscillations in a network model of the olfactory bulb. J. Neurophysiol. 95,
2678–2691 (2006).

[11] Eeckman, F. H. & Freeman, W. J. Correlations between unit firing and EEG in the
rat olfactory system. Brain Res 528, 238–244 (1990).

[12] Cleland, T. A., Johnson, B. A., Leon, M. & Linster, C. Relational representation in
the olfactory system. Proc. Natl. Acad. Sci. U.S.A. 104, 1953–1958 (2007).

[13] Cleland, T. A. et al. Sequential mechanisms underlying concentration invariance in
biological olfaction. Front Neuroeng 4, 21 (2011).

[14] Banerjee, A. et al. An interglomerular circuit gates glomerular output and implements gain control in the mouse olfactory bulb. Neuron 87, 193–207 (2015).

25


-----

[15] Storace, D. A. & Cohen, L. B. Measuring the olfactory bulb input-output transformation reveals a contribution to the perception of odorant concentration invariance.
_Nat Commun 8, 81 (2017)._

[16] Storace, D. A., Cohen, L. B. & Choi, Y. Using genetically encoded voltage indicators
(GEVIs) to study the input-output transformation of the mammalian olfactory bulb.
_Front Cell Neurosci 13, 342 (2019)._

[17] Frederick, D. E. et al. Gamma and beta oscillations define a sequence of neurocognitive modes present in odor processing. J. Neurosci. 36, 7750–7767 (2016).

[18] Kay, L. M. Circuit oscillations in odor perception and memory. Prog. Brain Res. 208,
223–251 (2014).

[19] Chatterjee, M., Perez de Los Cobos Pallares, F., Loebel, A., Lukas, M. & Egger, V.
Sniff-like patterned input results in long-term plasticity at the rat olfactory bulb
mitral and tufted cell to granule cell synapse. Neural Plast. 2016, 9124986 (2016).

[20] Strowbridge, B. W. Role of cortical feedback in regulating inhibitory microcircuits.
_Ann. N. Y. Acad. Sci. 1170, 270–274 (2009)._

[21] Gao, Y. & Strowbridge, B. W. Long-term plasticity of excitatory inputs to granule
cells in the rat olfactory bulb. Nat. Neurosci. 12, 731–733 (2009).

[22] Sailor, K. A. et al. Persistent structural plasticity optimizes sensory information
processing in the olfactory bulb. Neuron 91, 384–396 (2016).

[23] Lepousez, G. et al. Olfactory learning promotes input-specific synaptic plasticity in
adult-born neurons. Proc Natl Acad Sci U S A 111, 13984–13989 (2014).

[24] Gheusi, G. & Lledo, P. M. Adult neurogenesis in the olfactory system shapes odor
memory and perception. Prog Brain Res 208, 157–175 (2014).

[25] Magavi, S. S., Mitchell, B. D., Szentirmai, O., Carter, B. S. & Macklis, J. D. Adult-born
and preexisting olfactory granule neurons undergo distinct experience-dependent
modifications of their olfactory responses in vivo. J Neurosci 25, 10729–10739 (2005).

[26] Herz, R. S. & Engen, T. Odor memory: review and analysis. Psychonomic Bulletin &
_Review 3, 300–313 (1996)._

[27] Stevenson, R. J., Case, T. I. & Tomiczek, C. Resistance to interference of olfactory
perceptual learning. The Psychological Record 57, 103–116 (2007).

[28] Imam, N. & Cleland, T. A. Rapid online learning and robust recall in a neuromorphic olfactory circuit. Nature Machine Intelligence 2, 181–191 (2020).

[29] Gronowitz, M. E., Liu, A., Qiu, Q., Yu, C. R. & Cleland, T. A. A physicochemical
model of odor sampling. PLoS Comput Biol 17, e1009054 (2021).

26


-----

[30] Xu, L. et al. Widespread receptor-driven modulation in peripheral olfactory coding.
_Science 368 (2020)._

[31] Zak, J. D., Reddy, G., Vergassola, M. & Murthy, V. N. Antagonistic odor interactions
in olfactory sensory neurons are widespread in freely breathing mice. Nat Commun
**11, 3350 (2020).**

[32] Pfister, P. et al. Odorant receptor inhibition is fundamental to odor encoding. Curr
_Biol 30, 2574–2587 (2020)._

[33] Inagaki, S., Iwata, R., Iwamoto, M. & Imai, T. Widespread inhibition, antagonism,
and synergy in mouse olfactory sensory neurons in vivo. Cell Rep 31, 107814 (2020).

[34] Wilson, D. A. & Stevenson, R. J. The fundamental role of memory in olfactory
perception. Trends Neurosci. 26, 243–247 (2003).

[35] Wilson, D. & Stevenson, R. Learning to smell: olfactory perception from neurobiology to
_behavior (Johns Hopkins University Press, United States, 2006)._

[36] Royet, J. P., Plailly, J., Saive, A. L., Veyrac, A. & Delon-Martin, C. The impact of
expertise in olfaction. Front Psychol 4, 928 (2013).

[37] Cleland, T. A., Narla, V. A. & Boudadi, K. Multiple learning parameters differentially regulate olfactory generalization. Behav. Neurosci. 123, 26–35 (2009).

[38] Tong, M. T., Peace, S. T. & Cleland, T. A. Properties and mechanisms of olfactory
learning and memory. Front Behav Neurosci 8, 238 (2014).

[39] Vinera, J. et al. Olfactory perceptual learning requires action of noradrenaline in
the olfactory bulb: comparison with olfactory associative learning. Learn. Mem. 22,
192–196 (2015).

[40] Mandairon, N., Sultan, S., Nouvian, M., Sacquet, J. & Didier, A. Involvement of
newborn neurons in olfactory associative learning? The operant or non-operant
component of the task makes all the difference. J. Neurosci. 31, 12455–12460 (2011).

[41] Kermen, F., Sultan, S., Sacquet, J., Mandairon, N. & Didier, A. Consolidation of
an olfactory memory trace in the olfactory bulb is required for learning-induced
survival of adult-born neurons and long-term memory. PLoS ONE 5, e12118 (2010).

[42] Grelat, A. et al. Adult-born neurons boost odor-reward association. Proc Natl Acad
_Sci U S A 115, 2514–2519 (2018)._

[43] Doucette, W. & Restrepo, D. Profound context-dependent plasticity of mitral cell
responses in olfactory bulb. PLoS Biol. 6, e258 (2008).

[44] Nunez-Parra, A., Li, A. & Restrepo, D. Coding odor identity and odor value in
awake rodents. Prog. Brain Res. 208, 205–222 (2014).

27


-----

[45] Ramirez-Gordillo, D., Ma, M. & Restrepo, D. Precision of classification of odorant
value by the power of olfactory bulb oscillations is altered by optogenetic silencing
of local adrenergic innervation. Front Cell Neurosci 12, 48 (2018).

[46] Mandairon, N. et al. Context-driven activation of odor representations in the absence of olfactory stimuli in the olfactory bulb and piriform cortex. Front Behav
_Neurosci 8, 138 (2014)._

[47] Herz, R. S. Odor-associative learning and emotion: effects on perception and behavior. Chem. Senses 30 Suppl 1, i250–251 (2005).

[48] Aqrabawi, A. J. & Kim, J. C. Hippocampal projections to the anterior olfactory
nucleus differentially convey spatiotemporal information during episodic odour
memory. Nat Commun 9, 2735 (2018).

[49] Aqrabawi, A. J. & Kim, J. C. Olfactory memory representations are stored in the
anterior olfactory nucleus. Nat Commun 11, 1246 (2020).

[50] Levinson, M. et al. Context-dependent odor learning requires the anterior olfactory
nucleus. Behav. Neurosci. 134, 332–343 (2020).

[51] Li, A., Rao, X., Zhou, Y. & Restrepo, D. Complex neural representation of odour
information in the olfactory bulb. Acta Physiol (Oxf) 228, e13333 (2020).

[52] Igarashi, K. M. et al. Parallel mitral and tufted cell pathways route distinct odor
information to different targets in the olfactory cortex. _J Neurosci 32, 7970–7985_
(2012).

[53] Zaidi, Q. et al. Perceptual spaces: mathematical structures to neural mechanisms. J.
_Neurosci. 33, 17597–17602 (2013)._

[54] Edelman, S. & Shahbazi, R. Renewing the respect for similarity. _Front Comput_
_Neurosci 6, 45 (2012)._

[55] Shepard, R. N. Toward a universal law of generalization for psychological science.
_Science 237, 1317–1323 (1987)._

[56] Clapper, J. P. Graded similarity in free categorization. Cognition 190, 1–19 (2019).

[57] Tversky, A. Features of similarity. Psychol Rev 84, 327–352 (1977).

[58] Cleland, T. A., Morse, A., Yue, E. L. & Linster, C. Behavioral models of odor similarity. Behav. Neurosci. 116, 222–231 (2002).

[59] Khan, R. M. et al. Predicting odor pleasantness from odorant structure: pleasantness
as a reflection of the physical world. J Neurosci 27, 10015–10023 (2007).

[60] Meister, M. On the dimensionality of odor space. eLife 4, e07865 (2015).

28


-----

[61] Victor, J. D., Rizvi, S. M. & Conte, M. M. Two representations of a high-dimensional
perceptual space. Vision Research 137, 1–23 (2017).

[62] Harnad, S. (ed.) Categorical Perception: The Groundwork of Cognition (Cambridge University Press, 1987).

[63] Goldstone, R. L. & Hendrickson, A. T. Categorical perception. WIREs Cognitive
_Science 1, 69–78 (2010)._

[64] Aschauer, D. & Rumpel, S. The sensory neocortex and associative memory. Current
_Topics in Behavioral Neurosciences 37, 177–211 (2018)._

[65] Locatelli, F. F., Fernandez, P. C. & Smith, B. H. Learning about natural variation of
odor mixtures enhances categorization in early olfactory processing. J Exp Biol 219,
2752–2762 (2016).

[66] Mombaerts, P. et al. Visualizing an olfactory sensory map. Cell 87, 675–686 (1996).

[67] Wachowiak, M. & Cohen, L. B. Representation of odorants by receptor neuron input
to the mouse olfactory bulb. Neuron 32, 723–735 (2001).

[68] Cooperstein, B. N. Advanced linear algebra. Textbooks in Mathematics (CRC Press,
2015), 2nd edn.

[69] Haddad, R. et al. Global features of neural activity in the olfactory system form a
parallel code that predicts olfactory behavior and perception. J Neurosci 30, 9017–
9026 (2010).

[70] Koulakov, A., Kolterman, B., Enikolopov, A. & Rinberg, D. In search of the structure
of human olfactory space. Frontiers in Systems Neuroscience 5, 65 (2011).

[71] Castro, J. B., Ramanathan, A. & Chennubhotla, C. S. Categorical dimensions of
human odor descriptor space revealed by non-negative matrix factorization. PLoS
_ONE 8, 1–16 (2013)._

[72] Zarzo, M. & Stanton, D. T. Identification of latent variables in a semantic odor
profile database using principal component analysis. Chemical Senses 31, 713–724
(2006).

[73] Berke, M. D., Field, D. J. & Cleland, T. A. The sparse structure of natural chemical
environments. In 2017 ISOCS/IEEE International Symposium on Olfaction and Elec_tronic Nose (ISOEN), 1–3 (2017)._

[74] Perez, M., Nowotny, T., d’Ettorre, P. & Giurfa, M. Olfactory experience shapes the
evaluation of odour similarity in ants: a behavioural and computational analysis.
_Proc Biol Sci 283 (2016)._

[75] Wright, G. A., Kottcamp, S. M. & Thomson, M. G. Generalization mediates sensitivity to complex odor features in the honeybee. PLoS One 3, e1704 (2008).

29


-----

[76] Daly, K. C., Chandra, S., Durtschi, M. L. & Smith, B. H. The generalization of an
olfactory-based conditioned response reveals unique but overlapping odour representations in the moth Manduca sexta. J Exp Biol 204, 3085–3095 (2001).

[77] Rabin, M. D. Experience facilitates olfactory quality discrimination. Percept Psy_chophys 44, 532–540 (1988)._

[78] Moreno, M. M. et al. Olfactory perceptual learning requires adult neurogenesis.
_Proc. Natl. Acad. Sci. U.S.A. 106, 17980–17985 (2009)._

[79] Forest, J. et al. Short-term availability of adult-born neurons for memory encoding.
_Nat Commun 10, 5609 (2019)._

[80] Sultan, S. et al. Learning-dependent neurogenesis in the olfactory bulb determines
long-term olfactory memory. FASEB J. 24, 2355–2363 (2010).

[81] Singer, W. & Lazar, A. Does the cerebral cortex exploit high-dimensional, non-linear
dynamics for information processing? Front Comput Neurosci 10, 99 (2016).

[82] Borthakur, A. & Cleland, T. A. Signal conditioning for learning in the wild. In
_Proceedings of the 7th Annual Neuro-Inspired Computational Elements Workshop (Asso-_
ciation for Computing Machinery, Albany, NY, USA, 2019).

[83] Bruni, L. E. Hierarchical categorical perception in sensing and cognitive processes.
_Biosemiotics 1, 113–130 (2008)._

[84] Mori, K., Nowycky, M. C. & Shepherd, G. M. Analysis of synaptic potentials in
mitral cells in the isolated turtle olfactory bulb. J. Physiol. (Lond.) 314, 295–309 (1981).

[85] Mori, K., Nowycky, M. C. & Shepherd, G. M. Electrophysiological analysis of mitral
cells in the isolated turtle olfactory bulb. J. Physiol. (Lond.) 314, 281–294 (1981).

[86] P´erez-Gay Ju´arez, F., Sicotte, T., Th´eriault, C. & Harnad, S. Category learning can
alter perception and its neural correlates. PLoS ONE 14, 1–29 (2019).

[87] Hahn, U. & Heit, E. Cognitive psychology of semantic similarity. _International_
_Encyclopedia of the Social and Behavioral Sciences 13878–13881 (2001)._

[88] Wedhorn, T. Manifolds, Sheaves, and Cohomology. Springer Stadium MathematikMaster (Springer Fachmedien Wiesbaden, 2016).

[89] Malek, E. Topology and geometry for physicists. PoS Modave2017, 002 (2018).

[90] Mac Lane, S. & Moerdijk, I. Sheaves in Geometry and Logic: A First Introduction to
_Topos Theory. Universitext (Springer-Verlag, 1992)._

[91] Moser, A. Y., Bizo, L. & Brown, W. Y. Olfactory generalization in detector dogs.
_Animals (Basel) 9 (2019)._

30


-----

[92] Bekinschtein, P. et al. Persistence of long-term memory storage requires a late protein synthesis- and BDNF- dependent phase in the hippocampus. Neuron 53, 261–
277 (2007).

[93] Bekinschtein, P. et al. BDNF is essential to promote persistence of long-term memory storage. Proc Natl Acad Sci U S A 105, 2711–2716 (2008).

[94] Dudai, Y., Karni, A. & Born, J. The Consolidation and Transformation of Memory.
_Neuron 88, 20–32 (2015)._

[95] Bellfy, L. & Kwapis, J. L. Molecular Mechanisms of Reconsolidation-Dependent
Memory Updating. Int J Mol Sci 21 (2020).

[96] Hackett, C., Choi, C., O’Brien, B., Shin, P. & Linster, C. Odor memory and discrimination covary as a function of delay between encoding and recall in rats. Chem
_Senses 40, 315–323 (2015)._

[97] Buseck, A., McPherson, K. & Linster, C. Olfactory recognition memory in mice
depends on task parameters. Behav Neurosci (2020).

[98] Freedman, K. G., Radhakrishna, S., Escanilla, O. & Linster, C. Duration and specificity of olfactory nonassociative memory. Chem Senses 38, 369–375 (2013).

[99] Tong, M. T., Kim, T. P. & Cleland, T. A. Kinase activity in the olfactory bulb is
required for odor memory consolidation. Learn. Mem. 25, 198–205 (2018).

[100] Linster, C. et al. Noradrenergic activity in the olfactory bulb is a key element for the
stability of olfactory memory. J Neurosci 40, 9260–9271 (2020).

[101] Proust, M. Swann’s Way (In Search of Lost Time, Vol. 1) (Penguin Classics, 2004).

[102] Linster, C., Johnson, B. A., Morse, A., Yue, E. & Leon, M. Spontaneous versus
reinforced olfactory discriminations. J Neurosci 22, 6842–6845 (2002).

[103] Tversky, A. & Gati, I. Similarity, separability, and the triangle inequality. Psychol
_Rev 89, 123–154 (1982)._

[104] Roberts, S. A. et al. Individual odour signatures that mice learn are shaped by
involatile major urinary proteins (MUPs). BMC Biol 16, 48 (2018).

[105] Thoß, M., Luzynski, K. C., Ante, M., Miller, I. & Penn, D. J. Major urinary protein
(MUP) profiles show dynamic changes rather than individual ’barcode’ signatures.
_Front Ecol Evol 3 (2015)._

[106] Bushdid, C., Magnasco, M. O., Vosshall, L. B. & Keller, A. Humans can discriminate
more than 1 trillion olfactory stimuli. Science 343, 1370–1372 (2014).

[107] Gerkin, R. C. & Castro, J. B. The number of olfactory stimuli that humans can
discriminate is still unknown. Elife 4, e08127 (2015).

31


-----

[108] Majid, A. & Kruspe, N. Hunter-gatherer olfaction is special. Curr Biol 28, 409–413
(2018).

[109] Lahiri, S., Sohl-Dickstein, J. & Ganguli, S. A universal tradeoff between power,
precision and speed in physical communication (2016). 1603.07758.

[110] Abraham, N. M. et al. Maintaining accuracy at the expense of speed: stimulus
similarity defines odor discrimination time in mice. Neuron 44, 865–876 (2004).

[111] Rinberg, D., Koulakov, A. & Gelperin, A. Speed-accuracy tradeoff in olfaction. Neu_ron 51, 351–358 (2006)._

[112] Bhattacharjee, A. S. et al. Similarity and strength of glomerular odor representations
define a neural metric of sniff-invariant discrimination time. Cell Rep 28, 2966–2978
(2019).

[113] Frederick, D. E. et al. Task-dependent behavioral dynamics make the case for temporal integration in multiple strategies during odor processing. _J. Neurosci. 37,_
4416–4426 (2017).

[114] Zariwala, H. A., Kepecs, A., Uchida, N., Hirokawa, J. & Mainen, Z. F. The limits of
deliberation in a perceptual decision task. Neuron 78, 339–351 (2013).

[115] Aqrabawi, A. J. et al. Top-down modulation of olfactory-guided behaviours by the
anterior olfactory nucleus pars medialis and ventral hippocampus. Nat Commun 7,
13721 (2016).

[116] Cleland, T. A. Early transformations in odor representation. Trends Neurosci. 33,
130–139 (2010).

[117] Beyeler, M., Rounds, E. L., Carlson, K. D., Dutt, N. & Krichmar, J. L. Neural correlates of sparse coding and dimensionality reduction. PLoS Comput Biol 15, e1006908
(2019).

[118] Olshausen, B. A. & Field, D. J. Sparse coding of sensory inputs. Curr Opin Neurobiol
**14, 481–487 (2004).**

[119] Borthakur, A. & Cleland, T. A. A spike time-dependent online learning algorithm
derived from biological olfaction. Front Neurosci 13, 656 (2019).

[120] Wesson, D. W. The tubular striatum. J Neurosci 40, 7379–7386 (2020).

[121] Schoonover, C. E., Ohashi, S. N., Axel, R. & Fink, A. J. P. Representational drift in
primary olfactory cortex. Nature 594, 541–546 (2021).

[122] Rule, M. E., O’Leary, T. & Harvey, C. D. Causes and consequences of representational drift. Curr Opin Neurobiol 58, 141–147 (2019).

[123] Rule, M. E. et al. Stable task information from an unstable neural population. Elife
**9 (2020).**

32


-----

[124] Deitch, D., Rubin, A. & Ziv, Y. Representational drift in the mouse visual cortex.
_Curr Biol 31, 4327–4339 (2021)._

[125] Driscoll, L. N., Pettit, N. L., Minderer, M., Chettih, S. N. & Harvey, C. D. Dynamic
reorganization of neuronal activity patterns in parietal cortex. Cell 170, 986–999
(2017).

[126] Ziv, Y. et al. Long-term dynamics of CA1 hippocampal place codes. Nat Neurosci 16,
264–266 (2013).

[127] Mankin, E. A., Diehl, G. W., Sparks, F. T., Leutgeb, S. & Leutgeb, J. K. Hippocampal CA2 activity patterns change over time to a larger extent than between spatial
contexts. Neuron 85, 190–201 (2015).

33


-----

