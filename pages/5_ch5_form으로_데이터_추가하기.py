import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://i.namu.wiki/i/R9GjiUEKY9snXwP9mqXDRsHkZ0yK5GVoJtFHEMCamYe5jd4FeIrcMMU6ZRuMnJ0Pckci7qhOhWhXLqqoRNfovfVysbJVtiO1J2aiwwlf6Xi-_KHpXCnkchch9GxvW5zVKf_5PeTtSQD5xm6yLrdMdw.webp",
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://i.namu.wiki/i/0KC24R7hvHoRQFaki5E9aJJc4h4NGh0szPAL9G7XDNPc6RiIdf7qCGfJkjrv3usF-ci2LLqQgxiFr1n7WTcbfYFKpWDnSyeVI8uUDBWwZ7-0V8hkd0VTPcms-NKxQXR3FEjJfQD8aJ40UW48XI8Qig.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://i.namu.wiki/i/7UtWDIVQMKLNRBNWu22wJXs6V7nQOVxNfL8WA2Hc54cFTG7g54JwgC15KQmEU38KL619H_tA5FjrsjQdLbhkltr_o4vNyn2QPgPNlNUpvmuNF15M_f-4-y7aDJ2wKs-QwvODfmcsNehO3S0ASrlj4w.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://i.namu.wiki/i/pkxLzKO8Qc2cljRAT93iMq7Emn1MlYCfTB_EJniomxCMRm-dZeHvay49fBBmFEkN9oXqfCGHEILDCf4Ukv7G19fCSPGlReWjVQAOU32za0gFjx7wWP4JMMq5vgDlLKTU0bA6y4FY5PWgLDItmiB03g.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://i.namu.wiki/i/xdKCqvexNrD96uPfuCLMSWQpho30h8yLqU7vOs7Xz0Olkb0UpZ8z47IqE4_63Vn1OyWISNe778I9hmCQrhjnNN6BeJ0tP_vlXLZYivUYHPamUmjnvy6MOjKbwx4ywXEzX0zLAj0vSvRMDPnBLoGnVg.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://i.namu.wiki/i/XWeCjbh9VZYMhmjI0rR-3ABIr66mg0iuxnfktX_D1zVJ5EdX8qcMauRPRbD0jzjhX2CaEFyIYH_L9qCOCjmPFeMIVIoGM0Ou_UikZhUSfwN745tQ7Minxxt81bTFMZKqw9fcF0qM-MOuGtBmhPB0hg.webp"
    },
]

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름")
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
        )
    image_url = st.text_input(label="포켓몬 이미지 URL")
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })

for i in range(0, len(pokemons), 3):
    row_pokemons = pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))
