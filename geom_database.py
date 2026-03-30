import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Département de Géomatique - CEDT G15",
    page_icon="🗺️",
    layout="wide"
)

geom1b_data = [
    ("ElHadji Seydou", "BADJI", "H"),
    ("Felix", "BANDIAKY", "H"),
    ("Ndéye Seynabou", "CAMARA", "F"),
    ("Ousseynou Ba", "CISSE", "H"),
    ("Mariama", "DIABONG", "F"),
    ("Alphousseyni", "DIAKHITE", "H"),
    ("Abdou Aziz", "DIALLO", "H"),
    ("Almamy", "DIATTA", "H"),
    ("Rokhy", "DIOCKOU", "F"),
    ("El Hadj Kader", "DIOP", "H"),
    ("Papa Demba", "DIOP", "H"),
    ("Seydina Alioune", "DIOP", "H"),
    ("Louise Saly", "DIOUF", "F"),
    ("Ndéye Fama", "DIOUF", "F"),
    ("Cheikh Manmour Insa", "DJIGO", "H"),
    ("Mame Binta", "FALL", "F"),
    ("Mame Fatou", "FALL", "F"),
    ("Landing", "GOUDIABY", "H"),
    ("Fasseye", "GUEYE", "F"),
    ("Khadissatou", "LAKH", "F"),
    ("Awa", "MBOUP", "F"),
    ("Fara C", "MENDY", "H"),
    ("Abdourakhmane", "NDAO", "H"),
    ("Abdou Diop", "NDIAYE", "H"),
    ("Adama", "NDIAYE", "F"),
    ("Aida", "NDIAYE", "F"),
    ("Babacar", "NDIAYE", "H"),
    ("Cheikh", "NDIAYE", "H"),
    ("Assane", "NDIONE", "H"),
    ("Youssoupha", "NDIONE", "H"),
    ("Mame Diarra", "NGOM", "F"),
    ("Cheikh", "NIANG", "H"),
    ("Ndéye Maty", "SALL", "F"),
    ("Assane", "SAMBE", "H"),
    ("Anais", "SAMBOU", "F"),
    ("Dieynaba", "SARR", "F"),
    ("Ndéye Arame", "SARR", "F"),
    ("Cheikh Tidiane", "SARR", "H"),
    ("Mame Diarra", "SENE", "F"),
    ("Boubou", "SY", "H"),
    ("Abdoulaye", "THIAM", "H"),
    ("Ndéye Aminata", "THIAW", "F"),
    ("Cheikh Ahmed Tidiane", "TOURE", "H"),
    ("Cheikh", "WADE", "H"),
    ("El Hadji Malick", "WADE", "H"),
]

geom1a_data = [
    ("Alpha Amadou", "BA", "H"),
    ("Mouhamed", "BA", "H"),
    ("Mohamed Moussa", "BAN", "H"),
    ("Ibrahima", "BOIRO", "H"),
    ("Adja seny", "Coly", "F"),
    ("Fama", "DIA", "F"),
    ("Cheikh Sadibou", "DIAKHAME", "H"),
    ("Aissatou", "DIALLO", "F"),
    ("Mame Awa", "DIALLO", "F"),
    ("Aissatou", "Diallo", "F"),
    ("Oumar", "Diallo", "H"),
    ("Mamadou Dickel", "DIARRA", "H"),
    ("Fallou", "DIATTA", "F"),
    ("Aida Betty", "DIENG", "F"),
    ("Ndéye Bathor", "DIEYE", "F"),
    ("Maodo Malick", "DIOP", "H"),
    ("Mame Khary", "Diop", "F"),
    ("Khady", "Diop", "F"),
    ("Awa", "DJITE", "F"),
    ("Mbaye", "DRAME", "H"),
    ("Fatimatou", "FAYE", "F"),
    ("Ndoumbé", "Faye", "F"),
    ("Ousmane", "GUEYE", "H"),
    ("Assane", "kâ", "H"),
    ("Mouhamed", "Kounta", "H"),
    ("Malick", "MANE", "H"),
    ("Ndéye", "MBENGUE", "F"),
    ("Assietou laye", "Mbengue", "F"),
    ("Marietou", "NDIAYE", "F"),
    ("Victor sady", "NDIAYE", "H"),
    ("Khalifa Ababacar", "NDIONE", "H"),
    ("Fatou", "Ndoye", "F"),
    ("Ndéye Fall", "SAMB", "F"),
    ("Ibrahima", "SANE", "H"),
    ("Fatou", "SECK", "F"),
    ("EL Malick", "SecK", "H"),
    ("Mame Rama", "SecK", "F"),
    ("Alphonse Cor", "SENE", "H"),
    ("Awa", "SOUARE", "F"),
    ("Cheikh Omar", "SOUARE", "H"),
    ("Mohamed Fadel", "SOW", "H"),
    ("Mamadou Diam", "SOW", "H"),
    ("Diarry", "TALL", "F"),
    ("Mame Diarra", "THIAM", "F"),
    ("Mame Guiniane", "THIAW", "F"),
    ("Aminata", "TOURE", "F"),
    ("Amadou", "KABA", "H"),
    ("abdoulaye", "diao", "H"),
]

geom2a_data = [
    ("Khadidiatou", "BA", "F"),
    ("Mame Diarra", "BA", "F"),
    ("Mouhamadou Malick", "Cissé", "H"),
    ("Adama Egudu", "Dia", "H"),
    ("Abdoulaye", "DIALLO", "H"),
    ("Diaraye", "DIALLO", "F"),
    ("Mouhamadou Fadilou Mbacké", "DIENG", "H"),
    ("Mohamed", "Dione", "H"),
    ("Ndeye Fatou", "DIOP", "F"),
    ("Serigne Fallou", "DIOP", "H"),
    ("Awa", "Diouf", "F"),
    ("Birane", "DIOUF", "H"),
    ("Fallou", "DIOUF", "H"),
    ("penda", "DIOUF", "F"),
    ("Mamadou", "DIOUF", "H"),
    ("Mareme", "Diouf", "F"),
    ("Seydina ababacar", "Dramé", "H"),
    ("Mamadou Lamine", "FALL", "H"),
    ("Mouhamed Lamine", "FALL", "H"),
    ("Rokhaya", "FALL", "F"),
    ("Khole Maurice", "FAYE", "H"),
    ("Maguette", "Gningue", "H"),
    ("Mbathio", "GUEYE", "F"),
    ("Alpha", "Kane", "H"),
    ("Aichatou", "Keita", "F"),
    ("Fatoumata", "Keita", "F"),
    ("Sokhna Maïmouna", "Keïta", "F"),
    ("Nourou", "LY", "H"),
    ("Ndeye Mareme", "Mbaye", "F"),
    ("Soda", "Mbaye", "F"),
    ("Mar", "Mboup", "H"),
    ("El hadji Babou", "NIASS", "H"),
    ("Saliou", "Ndiaye", "H"),
    ("Mame Awa", "NDOUR", "F"),
    ("Lassana", "NDOUR", "H"),
    ("Fatou", "NGOM", "F"),
    ("Mame Birame", "NGOM", "H"),
    ("Seynabou", "NGOM", "F"),
    ("Ousmane", "Sall", "H"),
    ("Mouhamed", "SAMBOU", "H"),
    ("Khady Dione", "SENE", "F"),
    ("Seynabou", "SENE", "F"),
    ("Bassirou", "Sow", "H"),
    ("Maimouna", "Sow", "F"),
    ("Mame diarra", "Sow", "F"),
    ("Ousseynou", "TALL", "H"),
    ("NDEYE ADAMA", "THIAM", "F"),
    ("Babacar", "THIAM", "H"),
    ("Habsatou", "THIAM", "F"),
    ("Mame waly", "Thiema", "F"),
    ("Mame Anta", "WADE", "F"),
]

geom2b_data = [
    ("Youssouf", "BA", "H"),
    ("Cheikh Amadou", "Ba", "H"),
    ("Ma awa", "Bayo", "F"),
    ("Daouda", "CISS", "H"),
    ("Adja", "COULIBALY", "F"),
    ("Nianguiri", "DEMBELE", "H"),
    ("Yakhara Ndiaye", "Deme", "F"),
    ("Aissatou", "DIAGNE", "F"),
    ("Malick", "Diakhate", "H"),
    ("Cherif Adramé", "DIALLO", "H"),
    ("Aly Momar", "Diallo", "H"),
    ("Mamadou Sounkarou", "Diarra", "H"),
    ("Marcel", "DIEDHIOU", "H"),
    ("Bineta", "DIOP", "F"),
    ("Sokhna", "DIOP", "F"),
    ("Ndèye Marième", "DIOP", "F"),
    ("Mansour", "DIOP", "H"),
    ("Mame Diarra", "DIOUF", "F"),
    ("Aminata", "Fall", "F"),
    ("Mamadou Sanoussi", "Fall", "H"),
    ("Mama konaté", "Faty", "F"),
    ("Fatou", "GAYE", "F"),
    ("Insa", "Goudiaby", "H"),
    ("Khabane", "GUEYE", "H"),
    ("Babacar", "Gueye", "H"),
    ("Mouhamadoul Moustapha", "Ka", "H"),
    ("Isseu", "KASSE", "F"),
    ("Ali", "KASSE", "H"),
    ("Pape Malick", "MBAYE", "H"),
    ("Iba", "MBENGUE", "H"),
    ("Falo", "MBOW", "H"),
    ("Ndeye maty", "Ndiaye", "F"),
    ("Abidine", "NDIAYE", "H"),
    ("Amy", "Ndiaye", "F"),
    ("Elhadj Oumar", "Ndiaye", "H"),
    ("Mouhamadou Abdoulaye", "NDIME", "H"),
    ("Safiyah", "NGOM", "F"),
    ("Sokhna Awa", "NIANG", "F"),
    ("Aminata", "Sagna", "F"),
    ("Malang", "Sané", "H"),
    ("Fatou", "Sarr", "F"),
    ("Djabou", "Sonko", "F"),
    ("Maimouna", "SOW", "F"),
    ("Aminata Minielle", "SOW", "F"),
    ("Diarry", "SOW", "F"),
    ("Ramata", "SY", "F"),
    ("Léontine Theodoria Élisabeth", "TENDENG", "F"),
    ("Ngagne demba", "Thiam", "H"),
    ("Sokhna Mame Diarra", "THIAM", "F"),
    ("Malick", "TOURE", "H"),
    ("Ndeye maguette", "TOURE", "F"),
    ("Lassana Ousmane", "TRAORE", "H"),
]

matieres_geom1_s1 = [
    "Programmation",
    "Base de données",
    "Cartographie",
    "Français",
    "Technique de base de la géographie",
    "Anglais",
    "Mathématique",
    "Dessin de plan",
    "Topographie",
]

matieres_geom1_s2 = [
    "Rapport Technique",
    "Levées Topographiques",
    "Statistique",
    "Implantation Base de Données",
    "Dessin Plan 3D",
    "Cartographie avec les logiciels libres",
    "Programmation",
    "Cartographie Thématique",
    "Création d'entreprise / Gestion d'Entreprise",
]

matieres_geom2_s1 = [
    "Système d'Information Géographique (SIG)",
    "Cartographie Thématique",
    "Photogrammétrie",
    "Télédétection",
    "Modèle Numérique de Terrain (MNT)",
    "Webmapping",
    "Planification de projet",
    "Implantation d'ouvrages",
    "Programmation",
    "Entrepreneuriat",
]

matieres_geom2_s2 = [
    "Programmation",
    "Encadrement projet",
    "Télédétection",
    "SIG",
    "Webmapping",
    "Projet Intégrateur",
    "Entrepreneuriat",
    "Base de données spatiale",
    "Topographie",
    "Planification de projet",
]

df_1b = pd.DataFrame(geom1b_data, columns=["Prénom", "Nom", "Sexe"])
df_1b["Classe"] = "GEOM 1B"
df_1b["Sexe"] = df_1b["Sexe"].map({"H": "Garçon", "F": "Fille"})

df_1a = pd.DataFrame(geom1a_data, columns=["Prénom", "Nom", "Sexe"])
df_1a["Classe"] = "GEOM 1A"
df_1a["Sexe"] = df_1a["Sexe"].map({"H": "Garçon", "F": "Fille"})

df_2a = pd.DataFrame(geom2a_data, columns=["Prénom", "Nom", "Sexe"])
df_2a["Classe"] = "GEOM 2A"
df_2a["Sexe"] = df_2a["Sexe"].map({"H": "Garçon", "F": "Fille"})

df_2b = pd.DataFrame(geom2b_data, columns=["Prénom", "Nom", "Sexe"])
df_2b["Classe"] = "GEOM 2B"
df_2b["Sexe"] = df_2b["Sexe"].map({"H": "Garçon", "F": "Fille"})

df_all = pd.concat([df_1b, df_1a, df_2a, df_2b], ignore_index=True)
df_all.index = range(1, len(df_all) + 1)

st.title("🗺️ Département de Géomatique — CEDT G15")
st.markdown("*Année 2025-2026 · Dakar Colobane*")
st.divider()

tabs = st.tabs(["👥 Étudiants", "📚 Matières", "📊 Statistiques"])

with tabs[0]:
    st.subheader("Liste des étudiants")

    col1, col2, col3 = st.columns(3)
    with col1:
        classe_filter = st.selectbox(
            "Classe",
            ["Toutes les classes", "GEOM 1A", "GEOM 1B", "GEOM 2A", "GEOM 2B"]
        )
    with col2:
        sexe_filter = st.selectbox("Genre", ["Tous", "Garçon", "Fille"])
    with col3:
        search = st.text_input("🔍 Rechercher un étudiant", placeholder="Nom ou prénom...")

    df_view = df_all.copy()

    if classe_filter != "Toutes les classes":
        df_view = df_view[df_view["Classe"] == classe_filter]
    if sexe_filter != "Tous":
        df_view = df_view[df_view["Sexe"] == sexe_filter]
    if search:
        mask = (
            df_view["Prénom"].str.contains(search, case=False, na=False) |
            df_view["Nom"].str.contains(search, case=False, na=False)
        )
        df_view = df_view[mask]

    df_view = df_view.reset_index(drop=True)
    df_view.index = range(1, len(df_view) + 1)

    st.markdown(f"*{len(df_view)} étudiant(s) trouvé(s)*")
    st.dataframe(df_view, use_container_width=True)

with tabs[1]:
    st.subheader("Programme des matières par classe et semestre")

    niveau = st.radio("Niveau", ["GEOM 1 (1A & 1B)", "GEOM 2 (2A & 2B)"], horizontal=True)

    if niveau == "GEOM 1 (1A & 1B)":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📘 Semestre 1")
            for i, m in enumerate(matieres_geom1_s1, 1):
                st.markdown(f"{i}. {m}")
        with c2:
            st.markdown("#### 📗 Semestre 2")
            for i, m in enumerate(matieres_geom1_s2, 1):
                st.markdown(f"{i}. {m}")
        st.info("ℹ️ Les matières sont communes aux classes GEOM 1A et GEOM 1B.")
    else:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📘 Semestre 1")
            for i, m in enumerate(matieres_geom2_s1, 1):
                st.markdown(f"{i}. {m}")
        with c2:
            st.markdown("#### 📗 Semestre 2")
            for i, m in enumerate(matieres_geom2_s2, 1):
                st.markdown(f"{i}. {m}")
        st.info("ℹ️ Les matières sont communes aux classes GEOM 2A et GEOM 2B.")

    st.divider()
    st.markdown("#### 👨‍🏫 Enseignants référents")
    profs_data = [
        ("Anglais", "Mr Samb", 1, 14),
        ("Technique de base de la Geographie", "Mr Kane", 1, 14),
        ("Programmation", "Mr Ndiaye", 1, 14),
        ("Cartographie Thématique", "Mr Ciss", 1, 14),
        ("Télédétection", "Mr Dia", 1, 14),
        ("Photogrammétrie", "Mr Diao", 1, 14),
        ("Modèle numérique de terrain", "Mr Diao", 1, 14),
        ("SIG", "Mr Ciss", 1, 14),
        ("Base de données spatiale", "Mr Fall", 1, 14),
        ("Topographie", "Mr Fall", 1, 14),
        ("Planification de projet", "Mr Fall", 1, 14),
    ]
    df_profs = pd.DataFrame(profs_data, columns=["Matière", "Professeur", "Coefficient", "Note de validation"])
    df_profs.index = range(1, len(df_profs) + 1)
    st.dataframe(df_profs, use_container_width=True)

with tabs[2]:
    st.subheader("Statistiques du département")

    total_col, fille_col, garcon_col = st.columns(3)
    with total_col:
        st.metric("👥 Total étudiants", len(df_all))
    with fille_col:
        nb_f = len(df_all[df_all["Sexe"] == "Fille"])
        st.metric("👩 Filles", nb_f)
    with garcon_col:
        nb_g = len(df_all[df_all["Sexe"] == "Garçon"])
        st.metric("👨 Garçons", nb_g)

    st.divider()

    st.markdown("#### Répartition par classe")
    stats_classe = df_all.groupby("Classe").agg(
        Total=("Nom", "count"),
        Filles=("Sexe", lambda x: (x == "Fille").sum()),
        Garçons=("Sexe", lambda x: (x == "Garçon").sum()),
    ).reset_index()
    stats_classe.index = range(1, len(stats_classe) + 1)
    st.dataframe(stats_classe, use_container_width=True)

    st.divider()

    st.markdown("#### Répartition par niveau")
    df_all["Niveau"] = df_all["Classe"].apply(lambda x: "1ère Année" if "1" in x else "2ème Année")
    stats_niv = df_all.groupby("Niveau").agg(
        Total=("Nom", "count"),
        Filles=("Sexe", lambda x: (x == "Fille").sum()),
        Garçons=("Sexe", lambda x: (x == "Garçon").sum()),
    ).reset_index()
    stats_niv.index = range(1, len(stats_niv) + 1)
    st.dataframe(stats_niv, use_container_width=True)

st.divider()
st.caption("CEDT G15 · Ministère de l'Emploi, de la Formation Professionnelle et Technique · Dakar Colobane")