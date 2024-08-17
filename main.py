import os
import subprocess
import time
import numpy as np

from ultralytics import YOLO

HOME = os.getcwd()


print(HOME)
os.chdir(HOME)

"""## Train model"""

subprocess.run(['yolo','task=classify', 'mode=train', 'model=weight/yolov8m-cls.pt','data=home/ldtan/ldtan/PLANT350K/data/plant','epochs=400', 'batch=16', 'imgsz=640', 'dropout=0.2', 'save=True', 'save_period=10'])


"""## Inference model"""
# Define the class names
class_names = [
    "abeliophyllum distichum",
    "acacia angustissima",
    "acacia auriculiformis",
    "acacia baileyana",
    "acacia berlandieri",
    "acacia brevispica",
    "acacia caven",
    "acacia cognata",
    "acacia confluens",
    "acacia confusa",
    "acacia dealbata",
    "acacia drepanolobium",
    "acacia etbaica",
    "acacia farnesiana",
    "acacia heterophylla",
    "acacia hockii",
    "acacia koaia",
    "acacia longifolia",
    "acacia mangium",
    "acacia mearnsii",
    "acacia melanoxylon",
    "acacia mellifera",
    "acacia nilotica",
    "acacia podalyriifolia",
    "acacia pravissima",
    "acacia pycnantha",
    "acacia redolens",
    "acacia retinodes",
    "acacia rigidula",
    "acacia saligna",
    "acacia senegalensis",
    "acacia seyal",
    "acacia simplex",
    "acacia spirorbis",
    "acacia tortilis",
    "acacia tortuosa",
    "acacia xanthophloea",
    "acalypha aristata",
    "acalypha crenata",
    "acalypha hispida",
    "acalypha indica",
    "acalypha integrifolia",
    "acalypha macrostachya",
    "acalypha virginica",
    "acalypha wilkesiana",
    "achyranthes aspera",
    "aciotis rubricaulis",
    "adenostyles alliariae",
    "adenostyles alpina",
    "adenostyles leucophylla",
    "adlumia fungosa",
    "adonis aestivalis",
    "adonis annua",
    "adonis flammea",
    "adonis microcarpa",
    "adonis pyrenaica",
    "adonis vernalis",
    "aegopodium podagraria",
    "aeschynomene americana",
    "aextoxicon punctatum",
    "aizoanthemum hispanicum",
    "aizoon canariense",
    "alcea biennis",
    "alcea rosea",
    "alcea setosa",
    "alibertia edulis",
    "alliaria petiolata",
    "alocasia baginda",
    "alocasia cucullata",
    "alocasia cuprea",
    "alocasia lauterbachiana",
    "alocasia longiloba",
    "alocasia macrorrhizos",
    "alocasia micholitziana",
    "alocasia odora",
    "alocasia reginula",
    "alocasia sanderiana",
    "alocasia wentii",
    "alocasia zebrina",
    "aloevera",
    "althaea cannabina",
    "althaea officinalis",
    "amla",
    "amruta balli",
    "anemone alpina",
    "anemone apennina",
    "anemone baldensis",
    "anemone blanda",
    "anemone canadensis",
    "anemone coronaria",
    "anemone halleri",
    "anemone hepatica",
    "anemone hortensis",
    "anemone hupehensis",
    "anemone montana",
    "anemone multifida",
    "anemone narcissiflora",
    "anemone nemorosa",
    "anemone palmata",
    "anemone patens",
    "anemone pavoniana",
    "anemone pratensis",
    "anemone pulsatilla",
    "anemone ranunculoides",
    "anemone rubra",
    "anemone sylvestris",
    "anemone tomentosa",
    "anemone trifolia",
    "anemone vernalis",
    "anemone virginiana",
    "anemone vitifolia",
    "anemone x hybrida",
    "angelica archangelica",
    "angelica atropurpurea",
    "angelica heterocarpa",
    "angelica lucida",
    "angelica razulii",
    "angelica sylvestris",
    "angostura granulosa",
    "anisocampium niponicum",
    "ansellia africana",
    "anthericum liliago",
    "anthericum ramosum",
    "anthurium andraeanum",
    "anthurium clarinervium",
    "anthurium crystallinum",
    "anthurium faustomirandae",
    "anthurium hookeri",
    "anthurium jenmanii",
    "anthurium salvinii",
    "anthurium scandens",
    "anthurium scherzerianum",
    "anthurium schlechtendalii",
    "anthurium veitchii",
    "anthurium warocqueanum",
    "antirhea borbonica",
    "aphelandra aurantiaca",
    "aphelandra scabra",
    "aphelandra sinclairiana",
    "aphelandra squarrosa",
    "apple",
    "aralia californica",
    "aralia elata",
    "aralia hispida",
    "aralia nudicaulis",
    "aralia racemosa",
    "aralia spinosa",
    "aristea abyssinica",
    "aristea ecklonii",
    "arthraxon hispidus",
    "ashwagandha",
    "aspilia mossambicensis",
    "aspilia pluriseta",
    "astydamia latifolia",
    "asystasia charmian",
    "asystasia gangetica",
    "asystasia mysorensis",
    "asystasia riparia",
    "atocion rupestre",
    "atractocarpus platyxylon",
    "azadirachta indica",
    "balsamorhiza sagittata",
    "banana",
    "barbarea intermedia",
    "barbarea orthoceras",
    "barbarea rupicola",
    "barbarea verna",
    "barbarea vulgaris",
    "barringtonia acutangula",
    "barringtonia asiatica",
    "bellium bellidioides",
    "bellpepper",
    "berula erecta",
    "betel piper",
    "bilimbi",
    "bismarckia nobilis",
    "bocoa prouacensis",
    "bonafousia undulata",
    "boscia angustifolia",
    "boscia coriacea",
    "boscia mossambicensis",
    "bourreria andrieuxii",
    "bourreria costaricensis",
    "bourreria succulenta",
    "breynia disticha",
    "breynia vitis-idaea",
    "broccoli",
    "brodiaea elegans",
    "browallia americana",
    "browallia speciosa",
    "butomus umbellatus",
    "cabbage",
    "calendula arvensis",
    "calendula officinalis",
    "calendula stellata",
    "calochortus eurycarpus",
    "calochortus gunnisonii",
    "calochortus leichtlinii",
    "calochortus luteus",
    "calochortus macrocarpus",
    "calochortus splendens",
    "calochortus tolmiei",
    "calodendrum capense",
    "calycanthus floridus",
    "calycanthus occidentalis",
    "calylophus hartwegii",
    "cantaloupe",
    "caraipa densifolia",
    "caraipa punctulata",
    "carrot",
    "carthamus caeruleus",
    "carthamus carduncellus",
    "carthamus lanatus",
    "carthamus mitissimus",
    "carthamus tinctorius",
    "cassava",
    "casuarina cunninghamiana",
    "casuarina equisetifolia",
    "cauliflower",
    "cedrela fissilis",
    "cedrela odorata",
    "cenchrus ciliaris",
    "cenchrus clandestinus",
    "cenchrus echinatus",
    "cenchrus longisetus",
    "cenchrus longispinus",
    "cenchrus purpureus",
    "cenchrus setaceus",
    "centranthus angustifolius",
    "centranthus calcitrapae",
    "centranthus lecoqii",
    "centranthus ruber",
    "cerbera manghas",
    "cereus forbesii",
    "cereus hexagonus",
    "cereus hildmannianus",
    "cereus jamacaru",
    "cereus repandus",
    "cereus uruguayanus",
    "chaerophyllum aromaticum",
    "chaerophyllum aureum",
    "chaerophyllum bulbosum",
    "chaerophyllum hirsutum",
    "chaerophyllum tainturieri",
    "chaerophyllum temulum",
    "chaerophyllum villarsii",
    "chamerion latifolium",
    "cirsium acaulon",
    "cirsium alsophilum",
    "cirsium altissimum",
    "cirsium arvense",
    "cirsium canum",
    "cirsium discolor",
    "cirsium dissectum",
    "cirsium eriophorum",
    "cirsium erisithales",
    "cirsium ferox",
    "cirsium filipendulum",
    "cirsium foliosum",
    "cirsium glabrum",
    "cirsium heterophyllum",
    "cirsium horridulum",
    "cirsium monspessulanum",
    "cirsium morisianum",
    "cirsium muticum",
    "cirsium oleraceum",
    "cirsium palustre",
    "cirsium rivulare",
    "cirsium spinosissimum",
    "cirsium texanum",
    "cirsium tuberosum",
    "cirsium undulatum",
    "cirsium vulgare",
    "citrus limon",
    "clethra alnifolia",
    "cobaea scandens",
    "coconut",
    "collomia grandiflora",
    "comptonia peregrina",
    "conoclinium coelestinum",
    "conostomium kenyense",
    "conostomium quadrangulare",
    "cordyla africana",
    "corispermum pallasii",
    "corn",
    "coryphantha elephantidens",
    "couroupita guianensis",
    "coussapoa villosa",
    "crotalaria brevidens",
    "crotalaria chrysochlora",
    "crotalaria deflersii",
    "crotalaria incana",
    "crotalaria juncea",
    "crotalaria laburnifolia",
    "crotalaria pallida",
    "crotalaria polysperma",
    "crotalaria pumila",
    "crotalaria retusa",
    "crotalaria spectabilis",
    "crotalaria uguenensis",
    "crotalaria verrucosa",
    "cryptopus elatus",
    "cryptostegia grandiflora",
    "cryptostegia madagascariensis",
    "cucumber",
    "cucurbita ficifolia",
    "cucurbita foetidissima",
    "cucurbita maxima",
    "cucurbita moschata",
    "cucurbita pepo",
    "curcuma",
    "curry leaf",
    "cyanotis somaliensis",
    "cymbalaria aequitriloba",
    "cymbalaria hepaticifolia",
    "cymbalaria muralis",
    "cyphostemma cyphopetalum",
    "cyphostemma juttae",
    "cyphostemma serpens",
    "cyrtanthus elatus",
    "cytinus hypocistis",
    "cytinus ruber",
    "dalbergia latifolia",
    "dalbergia melanoxylon",
    "dalbergia retusa",
    "dalbergia sissoo",
    "dalea purpurea",
    "danthonia decumbens",
    "daphne alpina",
    "daphne cneorum",
    "daphne gnidium",
    "daphne laureola",
    "daphne mezereum",
    "daphne odora",
    "daphne oleoides",
    "daphne sericea",
    "daphne striata",
    "daphne tangutica",
    "daucus carota",
    "daucus muricatus",
    "daucus pusillus",
    "declieuxia fruticosa",
    "dendrobium anosmum",
    "dendrobium aphyllum",
    "dendrobium chrysotoxum",
    "dendrobium closterium",
    "dendrobium crumenatum",
    "dendrobium kingianum",
    "dendrobium moschatum",
    "dendrobium munificum",
    "dendrobium nobile",
    "dendrobium spp",
    "dendrobium thyrsiflorum",
    "dendrobium victoriae-reginae",
    "diascia rigescens",
    "diascia vigilis",
    "diatelia tuberaria",
    "dierama pulcherrimum",
    "diervilla lonicera",
    "diervilla sessilifolia",
    "dischidia nummularia",
    "dischidia ovata",
    "dorotheanthus bellidiformis",
    "dracontium polyphyllum",
    "dracophyllum verticillatum",
    "dryas octopetala",
    "dryopteris aemula",
    "dryopteris affinis",
    "dryopteris carthusiana",
    "dryopteris cristata",
    "dryopteris cycadina",
    "dryopteris dilatata",
    "dryopteris erythrosora",
    "dryopteris expansa",
    "dryopteris filix-mas",
    "dryopteris fragrans",
    "dryopteris intermedia",
    "dryopteris marginalis",
    "dryopteris sieboldii",
    "dryopteris villarii",
    "dryopteris wallichiana",
    "dubouzetia campanulata",
    "dubouzetia confusa",
    "duchesnea indica",
    "egeria densa",
    "eggplant",
    "elephantopus elatus",
    "elodea canadensis",
    "empetrum nigrum",
    "empetrum rubrum",
    "entada gigas",
    "entada phaseoloides",
    "epipactis atrorubens",
    "epipactis gigantea",
    "epipactis helleborine",
    "epipactis leptochila",
    "epipactis microphylla",
    "epipactis muelleri",
    "epipactis palustris",
    "epipactis phyllanthes",
    "epipactis purpurata",
    "eranthemum pulchellum",
    "erechtites hieraciifolius",
    "erechtites minima",
    "erianthemum dregei",
    "eritrichium nanum",
    "erucastrum gallicum",
    "erucastrum incanum",
    "erucastrum nasturtiifolium",
    "erycina pusilla",
    "eucryphia cordifolia",
    "falcaria vulgaris",
    "falcataria moluccana",
    "faujasia salicifolia",
    "fedia cornucopiae",
    "fedia graciliflora",
    "fernelia buxifolia",
    "fibigia clypeata",
    "fittonia albivenis",
    "fragaria chiloensis",
    "fragaria moschata",
    "fragaria vesca",
    "fragaria virginiana",
    "fragaria viridis",
    "fragaria x ananassa",
    "freesia alba",
    "freesia refracta",
    "freesia x hybrida",
    "freycinetia cumingiana",
    "galangal",
    "galega officinalis",
    "galega orientalis",
    "ganike",
    "garrya elliptica",
    "geniostoma borbonicum",
    "geropogon hybridus",
    "ginger",
    "gomphocarpus fruticosus",
    "gomphocarpus integer",
    "gomphocarpus physocarpus",
    "goniolimon tataricum",
    "groenlandia densa",
    "guaiacum officinale",
    "guaiacum sanctum",
    "guarea gomma",
    "guatteria aeruginosa",
    "guatteria amplifolia",
    "guatteria anteridifera",
    "guatteria citriodora",
    "guatteria dolichopoda",
    "guatteria punctata",
    "guava",
    "guizotia abyssinica",
    "gymnosporia putterlickioides",
    "gynura aurantiaca",
    "gynura procumbens",
    "hackelia velutina",
    "haplophyton crooksii",
    "harpachne schimperi",
    "hebe andersonii",
    "hebe brachysiphon",
    "hebe franciscana",
    "hebe ochracea",
    "hebe salicifolia",
    "helicodiceros muscivorus",
    "helminthotheca echioides",
    "hepatica nobilis",
    "herbertia lahue",
    "hernandia cordigera",
    "hernandia mascarenensis",
    "hernandia nymphaeifolia",
    "heteromorpha arborescens",
    "hippophae rhamnoides",
    "holodiscus discolor",
    "honckenya peploides",
    "humulus lupulus",
    "hunnemannia fumariifolia",
    "hyoscyamus albus",
    "hyoscyamus niger",
    "hyoseris radiata",
    "hypericum androsaemum",
    "hypericum annulatum",
    "hypericum australe",
    "hypericum balearicum",
    "hypericum calycinum",
    "hypericum canariense",
    "hypericum coris",
    "hypericum elodes",
    "hypericum empetrifolium",
    "hypericum frondosum",
    "hypericum hircinum",
    "hypericum hirsutum",
    "hypericum humifusum",
    "hypericum hypericoides",
    "hypericum hyssopifolium",
    "hypericum kalmianum",
    "hypericum lanceolatum",
    "hypericum linariifolium",
    "hypericum maculatum",
    "hypericum montanum",
    "hypericum mutilum",
    "hypericum nummularium",
    "hypericum olympicum",
    "hypericum patulum",
    "hypericum perfoliatum",
    "hypericum perforatum",
    "hypericum prolificum",
    "hypericum pulchrum",
    "hypericum punctatum",
    "hypericum revolutum",
    "hypericum richeri",
    "hypericum tetrapetalum",
    "hypericum tetrapterum",
    "hypericum tomentosum",
    "hypericum triquetrifolium",
    "hypericum x hidcoteense",
    "hypericum x inodorum",
    "ibicella lutea",
    "illicium floridanum",
    "illicium verum",
    "iva annua",
    "iva frutescens",
    "iva xanthiifolia",
    "kale",
    "keckiella cordifolia",
    "kigelia africana",
    "kniphofia linearifolia",
    "kniphofia uvaria",
    "lactuca alpina",
    "lactuca biennis",
    "lactuca canadensis",
    "lactuca floridana",
    "lactuca macrophylla",
    "lactuca muralis",
    "lactuca perennis",
    "lactuca plumieri",
    "lactuca saligna",
    "lactuca sativa",
    "lactuca serriola",
    "lactuca tenerrima",
    "lactuca viminea",
    "lactuca virosa",
    "lagenaria siceraria",
    "lagenaria sphaerica",
    "lamium album",
    "lamium amplexicaule",
    "lamium bifidum",
    "lamium flexuosum",
    "lamium galeobdolon",
    "lamium garganicum",
    "lamium hybridum",
    "lamium maculatum",
    "lamium orvala",
    "lamium purpureum",
    "lapageria rosea",
    "lapsana communis",
    "lathraea clandestina",
    "lathraea squamaria",
    "lavandula angustifolia",
    "lavandula canariensis",
    "lavandula dentata",
    "lavandula latifolia",
    "lavandula minutolii",
    "lavandula multifida",
    "lavandula pinnata",
    "lavandula spp",
    "lavandula stoechas",
    "lavandula x intermedia",
    "leersia oryzoides",
    "leersia virginica",
    "leonitis nepetifolia",
    "leptinella potentillina",
    "leucophyta brownii",
    "limbarda crithmoides",
    "limnanthes douglasii",
    "limonia acidissima",
    "liriodendron chinensis",
    "liriodendron tulipifera",
    "liriope muscari",
    "lithodora fruticosa",
    "lithops aucampiae",
    "lithops fulviceps",
    "lithops karasmontana",
    "lithops marmorata",
    "lithops olivacea",
    "lithops pseudotruncatella",
    "lithops spp",
    "lomatia ferruginea",
    "longbeans",
    "loropetalum chinense",
    "luffa acutangula",
    "luffa cylindrica",
    "lupinus albifrons",
    "lupinus albus",
    "lupinus angustifolius",
    "lupinus arboreus",
    "lupinus argenteus",
    "lupinus bicolor",
    "lupinus chamissonis",
    "lupinus cosentinii",
    "lupinus diffusus",
    "lupinus formosus",
    "lupinus hirsutissimus",
    "lupinus luteus",
    "lupinus micranthus",
    "lupinus nootkatensis",
    "lupinus perennis",
    "lupinus pilosus",
    "lupinus polyphyllus",
    "lupinus subcarnosus",
    "lupinus texensis",
    "lupinus x regalis",
    "lycoris radiata",
    "lycoris squamigera",
    "lyonothamnus floribundus",
    "macrosyringion longiflorum",
    "maerua angolensis",
    "maerua triphylla",
    "maianthemum bifolium",
    "maianthemum canadense",
    "maianthemum racemosum",
    "maianthemum stellatum",
    "maianthemum trifolium",
    "mango",
    "margaritopsis haematocarpa",
    "maurandya barclayana",
    "mauritia flexuosa",
    "maytenus boaria",
    "maytenus ilicifolia",
    "mazus pumilus",
    "mecardonia procumbens",
    "melampodium divaricatum",
    "melampodium leucanthum",
    "melampodium perfoliatum",
    "melilotus albus",
    "melilotus altissimus",
    "melilotus indicus",
    "melilotus italicus",
    "melilotus officinalis",
    "melilotus spicatus",
    "melilotus sulcatus",
    "melon",
    "mentha",
    "mercurialis ambigua",
    "mercurialis annua",
    "mercurialis perennis",
    "mercurialis tomentosa",
    "mertensia ciliata",
    "mertensia maritima",
    "mertensia paniculata",
    "mertensia virginica",
    "metasequoia glyptostroboides",
    "meum athamanticum",
    "microchloa kunthii",
    "mitella diphylla",
    "moehringia ciliata",
    "moehringia lateriflora",
    "moehringia muscosa",
    "moehringia pentandra",
    "moehringia trinervia",
    "montanoa hibiscifolia",
    "morinda citrifolia",
    "mussaenda arcuata",
    "mussaenda erythrophylla",
    "mussaenda frondosa",
    "mussaenda philippica",
    "mussaenda pubescens",
    "myosoton aquaticum",
    "myosurus minimus",
    "nandina domestica",
    "narthecium ossifragum",
    "neobuxbaumia polylopha",
    "neolamarckia cadamba",
    "neotinea conica",
    "neotinea lactea",
    "neotinea maculata",
    "neotinea tridentata",
    "neotinea ustulata",
    "nepenthes alata",
    "nepenthes mirabilis",
    "nepenthes spp",
    "nepenthes truncata",
    "nepenthes vieillardii",
    "nepenthes x neglecta",
    "nephrolepis abrupta",
    "nephrolepis biserrata",
    "nephrolepis cordifolia",
    "nephrolepis exaltata",
    "nephrolepis falcata",
    "noccaea caerulescens",
    "noccaea montana",
    "noccaea rotundifolia",
    "nothofagus alpina",
    "nothofagus antarctica",
    "nothofagus betuloides",
    "nothofagus dombeyi",
    "nothofagus nitida",
    "nothofagus obliqua",
    "nothofagus pumilio",
    "nyctaginia capitata",
    "nymphaea alba",
    "nymphaea ampla",
    "nymphaea candida",
    "nymphaea lotus",
    "nymphaea mexicana",
    "nymphaea nouchali",
    "nymphaea odorata",
    "nymphaea rubra",
    "nymphaea tetragona",
    "nymphoides indica",
    "nymphoides peltata",
    "ocimum sanctum",
    "oldenlandia corymbosa",
    "oncostema elongata",
    "oncostema peruviana",
    "ophrys apifera",
    "ophrys arachnitiformis",
    "ophrys araneola",
    "ophrys aranifera",
    "ophrys aveyronensis",
    "ophrys aymoninii",
    "ophrys bertolonii",
    "ophrys bombyliflora",
    "ophrys catalaunica",
    "ophrys druentica",
    "ophrys exaltata",
    "ophrys fuciflora",
    "ophrys fusca",
    "ophrys incubacea",
    "ophrys insectifera",
    "ophrys lunulata",
    "ophrys lupercalis",
    "ophrys lutea",
    "ophrys morisii",
    "ophrys occidentalis",
    "ophrys passionis",
    "ophrys provincialis",
    "ophrys pseudoscolopax",
    "ophrys saratoi",
    "ophrys scolopax",
    "ophrys speculum",
    "ophrys sulcata",
    "ophrys tenthredinifera",
    "ophrys virescens",
    "orange",
    "oreopteris limbosperma",
    "osmunda cinnamomea",
    "osmunda claytoniana",
    "osmunda regalis",
    "othonna capensis",
    "oxydendrum arboreum",
    "paddy",
    "paederia foetida",
    "paederota bonarota",
    "pancratium canariense",
    "pancratium illyricum",
    "pancratium maritimum",
    "papaver alpinum",
    "papaver argemone",
    "papaver atlanticum",
    "papaver croceum",
    "papaver dubium",
    "papaver hybridum",
    "papaver nudicaule",
    "papaver orientale",
    "papaver pseudoorientale",
    "papaver rhaeticum",
    "papaver rhoeas",
    "papaver rupifragum",
    "papaver somniferum",
    "papaya",
    "patzkea paniculata",
    "pelargonium alchemilloides",
    "pelargonium capitatum",
    "pelargonium crispum",
    "pelargonium echinatum",
    "pelargonium glechomoides",
    "pelargonium grandiflorum",
    "pelargonium graveolens",
    "pelargonium inquinans",
    "pelargonium odoratissimum",
    "pelargonium panduriforme",
    "pelargonium peltatum",
    "pelargonium quercifolium",
    "pelargonium quinquelobatum",
    "pelargonium sidoides",
    "pelargonium spp",
    "pelargonium tomentosum",
    "pelargonium x asperum",
    "pelargonium x hortorum",
    "pelargonium x hybridum",
    "pelargonium zonale",
    "peper chili",
    "peperomia albovittata",
    "peperomia argyreia",
    "peperomia caperata",
    "peperomia clusiifolia",
    "peperomia columella",
    "peperomia dolabriformis",
    "peperomia ferreyrae",
    "peperomia graveolens",
    "peperomia maculosa",
    "peperomia magnoliifolia",
    "peperomia obtusifolia",
    "peperomia pecuniifolia",
    "peperomia pellucida",
    "peperomia polybotrya",
    "peperomia prostrata",
    "peperomia quadrangularis",
    "peperomia rotundifolia",
    "peperomia serpens",
    "peperomia tetragona",
    "peperomia verticillata",
    "pereskia aculeata",
    "pereskia bleo",
    "pereskia grandifolia",
    "perovskia abrotanoides",
    "perovskia atriplicifolia",
    "petiveria alliacea",
    "phalaris aquatica",
    "phalaris arundinacea",
    "phalaris canariensis",
    "phalaris coerulescens",
    "phalaris minor",
    "phalaris paradoxa",
    "phedimus aizoon",
    "phedimus spurius",
    "phedimus stellatus",
    "phyllanthus acidus",
    "phyllanthus amarus",
    "phyllanthus emblica",
    "phyllanthus epiphyllanthus",
    "phyllanthus fischeri",
    "phyllanthus mimosoides",
    "phyllanthus niruri",
    "phyllanthus niruroides",
    "phyllanthus phillyreifolius",
    "phyllanthus reticulatus",
    "phyllanthus suffrutescens",
    "phyllanthus tenellus",
    "phyllanthus urinaria",
    "pilocarpus racemosus",
    "pilosocereus chrysostele",
    "pilosocereus pachycladus",
    "pilosocereus royeni",
    "pineapple",
    "piriqueta cistoides",
    "pleurospermum austriacum",
    "pogonophora schomburgkiana",
    "pomelo",
    "pongamia pinnata",
    "potato",
    "prosopis alba",
    "prosopis farcta",
    "prosopis glandulosa",
    "prosopis juliflora",
    "prosopis pallida",
    "prosopis pubescens",
    "pterocephalus perennis",
    "pumpkin",
    "punica granatum",
    "pyracantha coccinea",
    "pyracantha koidzumii",
    "pyracantha rogersiana",
    "radish",
    "raphia farinifera",
    "rhodanthe chlorocephala",
    "rhodothamnus chamaecistus",
    "rosa sinensis",
    "rumohra adiantiformis",
    "sagittaria graminea",
    "sagittaria lancifolia",
    "sagittaria latifolia",
    "sagittaria montevidensis",
    "sagittaria sagittifolia",
    "sagotia racemosa",
    "sasa palmata",
    "schefflera actinophylla",
    "schefflera arboricola",
    "schefflera decaphylla",
    "schefflera heptaphylla",
    "schefflera morototoni",
    "schefflera spp",
    "schinopsis balansae",
    "schkuhria pinnata",
    "secale cereale",
    "sedum acre",
    "sedum adolphii",
    "sedum albomarginatum",
    "sedum album",
    "sedum allantoides",
    "sedum alpestre",
    "sedum amplexicaule",
    "sedum andegavense",
    "sedum anglicum",
    "sedum annuum",
    "sedum atratum",
    "sedum brevifolium",
    "sedum burrito",
    "sedum caeruleum",
    "sedum caespitosum",
    "sedum cepaea",
    "sedum clavatum",
    "sedum compressum",
    "sedum cyaneum",
    "sedum dasyphyllum",
    "sedum decumbens",
    "sedum dendroideum",
    "sedum divergens",
    "sedum forsterianum",
    "sedum furfuraceum",
    "sedum glaucophyllum",
    "sedum hernandezii",
    "sedum hirsutum",
    "sedum hispanicum",
    "sedum japonicum",
    "sedum kamtschaticum",
    "sedum lanceolatum",
    "sedum laxum",
    "sedum lineare",
    "sedum litoreum",
    "sedum makinoi",
    "sedum mexicanum",
    "sedum montanum",
    "sedum moranense",
    "sedum morganianum",
    "sedum multiceps",
    "sedum niveum",
    "sedum nussbaumerianum",
    "sedum obtusatum",
    "sedum ochroleucum",
    "sedum oreganum",
    "sedum pachyphyllum",
    "sedum palmeri",
    "sedum praealtum",
    "sedum pulchellum",
    "sedum rubens",
    "sedum rubrotinctum",
    "sedum rupestre",
    "sedum sarmentosum",
    "sedum sediforme",
    "sedum sexangulare",
    "sedum spathulifolium",
    "sedum ternatum",
    "sedum villosum",
    "selenicereus anthonyanus",
    "selenicereus grandiflorus",
    "shallot",
    "smilax anceps",
    "smilax aspera",
    "smilax bona-nox",
    "smilax china",
    "smilax excelsa",
    "smilax glauca",
    "smilax herbacea",
    "smilax laurifolia",
    "smilax rotundifolia",
    "smilax tamnoides",
    "soybeans",
    "spergularia rubra",
    "spinach",
    "stanleya pinnata",
    "stemodia verticillata",
    "stenanona costaricensis",
    "stenocactus multicostatus",
    "stoebe passerinoides",
    "striga asiatica",
    "strongylodon macrobotrys",
    "sweet potatoes",
    "tagetes erecta",
    "tagetes lemmonii",
    "tagetes lucida",
    "tagetes lunulata",
    "tagetes minuta",
    "tagetes patula",
    "tagetes tenuifolia",
    "telekia speciosa",
    "tephrocactus geometricus",
    "tetraclinis articulata",
    "thapsia garganica",
    "thapsia villosa",
    "thesium alpinum",
    "thesium humifusum",
    "thesium linophyllon",
    "thesium pyrenaicum",
    "tobacco",
    "trachelospermum asiaticum",
    "trachelospermum jasminoides",
    "tradescantia cerinthoides",
    "tradescantia crassifolia",
    "tradescantia fluminensis",
    "tradescantia occidentalis",
    "tradescantia ohiensis",
    "tradescantia pallida",
    "tradescantia sillamontana",
    "tradescantia spathacea",
    "tradescantia subaspera",
    "tradescantia virginiana",
    "tradescantia x andersoniana",
    "tradescantia zebrina",
    "triadica sebifera",
    "trifolium alexandrinum",
    "trifolium alpestre",
    "trifolium alpinum",
    "trifolium angustifolium",
    "trifolium arvense",
    "trifolium aureum",
    "trifolium badium",
    "trifolium campestre",
    "trifolium cherleri",
    "trifolium dubium",
    "trifolium fragiferum",
    "trifolium glomeratum",
    "trifolium hirtum",
    "trifolium hybridum",
    "trifolium incarnatum",
    "trifolium lappaceum",
    "trifolium medium",
    "trifolium michelianum",
    "trifolium micranthum",
    "trifolium montanum",
    "trifolium nigrescens",
    "trifolium ochroleucon",
    "trifolium pallescens",
    "trifolium pannonicum",
    "trifolium patens",
    "trifolium pratense",
    "trifolium purpureum",
    "trifolium repens",
    "trifolium resupinatum",
    "trifolium rubens",
    "trifolium scabrum",
    "trifolium spadiceum",
    "trifolium spumosum",
    "trifolium squamosum",
    "trifolium stellatum",
    "trifolium striatum",
    "trifolium subterraneum",
    "trifolium thalii",
    "trifolium tomentosum",
    "trimezia martinicensis",
    "trinia glauca",
    "uncinia rubra",
    "urera baccifera",
    "vaccaria hispanica",
    "vangueria madagascariensis",
    "vanilla planifolia",
    "vanilla pompona",
    "vepris lanceolata",
    "viscaria alpina",
    "viscaria vulgaris",
    "vismia cayennensis",
    "vismia macrophylla",
    "vismia sessilifolia",
    "waterapple",
    "watermelon",
    "wigandia caracasana",
    "wigandia urens",
    "wodyetia bifurcata",
    "xylococcus bicolor",
    "xylopia crinita",
    "xylopia frutescens",
    "xylopia nitida",
    "xylopia sericea",
    "zaleya pentandra",
    "zamia furfuracea",
    "zamia pumila",
    "zamioculcas zamiifolia",
    "zannichellia palustris"
  ]

# start_inf_time = time.time()
model = YOLO('runs/classify/train/weights/best.pt')

class_inference_times = []
class_valid_times = []
class_inf_top1_accuracies = []
class_val_top1_accuracies = []

for class_name in class_names:
    class_start_time = time.time()
    class_path = os.path.join('data/plant/test/', class_name)
    class_results = model(source=class_path, imgsz=640)
    class_inference_time = time.time() - class_start_time
    class_inference_times.append(class_inference_time)

    class_top1_confidences = []
    for result in class_results:
        top1_conf = result.probs.top1conf.cpu().numpy().item()
        class_top1_confidences.append(top1_conf)
    class_top1_accuracy = np.mean(class_top1_confidences)
    class_inf_top1_accuracies.append(class_top1_accuracy)

total_inference_time = time.time() - start_inf_time
average_class_inference_time = np.mean(class_inference_times)
average_inf_top1_accuracy = np.mean(class_inf_top1_accuracies)


"""## Save inference results"""
with open('inference.txt', 'w') as f:
    f.write("Inference Results:\n")
    f.write(f"Total number of classes: {len(class_names):<20}\n")
    f.write(f"Total Inference Time: {total_inference_time:.2f} seconds\n")
    f.write(f"Average Class Inference Time: {average_class_inference_time:.2f} seconds\n")
    f.write(f"Accuracy: {average_inf_top1_accuracy:.3f}\n")


"""## Validating model"""
start_val_time = time.time()
for class_name in class_names:
    class_start_time = time.time()
    class_path = os.path.join('data/plant/valid/', class_name)
    class_results = model(source=class_path, imgsz=640)
    class_inference_time = time.time() - class_start_time
    class_valid_times.append(class_inference_time)
    class_top1_confidences = []
    for result in class_results:
        top1_conf = result.probs.top1conf.cpu().numpy().item()
        class_top1_confidences.append(top1_conf)
    class_top1_accuracy = np.mean(class_top1_confidences)
    class_val_top1_accuracies.append(class_top1_accuracy)

total_validation_time = time.time() - start_val_time
average_class_validation_time = np.mean(class_valid_times)
average_val_top1_accuracy = np.mean(class_val_top1_accuracies)

"""## Save validation results"""
with open('valid.txt', 'w') as f:
    f.write("Validation Results:\n")
    f.write(f"Total number of classes: {len(class_names):<20}\n")
    f.write(f"Total Validation Time: {total_validation_time:.2f} seconds\n")
    f.write(f"Average Class Validation Time: {average_class_validation_time:.2f} seconds\n")
    f.write(f"Accuracy: {average_val_top1_accuracy:.3f}\n")
