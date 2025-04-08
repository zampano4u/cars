import streamlit as st

# pip install streamlit

# ----------------------------- Data Definition -----------------------------
# PART 1 : questions 1 ~ 8
cars_mapping_part1 = [
    {
        "id": 1,
        "question_ko": "사람들과의 관계",
        "question_en": "Relating to People",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 사람들과의 관계에서 어려움이나 이상이 있다는 증거가 전혀 없습니다. 아동의 행동은 연령에 적절합니다. 다소 수줍음을 타거나, 까다롭거나, 지시를 받는 것에 불쾌감을 표현할 수는 있지만, 이는 비전형적인 수준이 아닙니다.",
                "text_en": "(1) No evidence of difficulty or abnormality in relating to people. The child’s behavior is appropriate for his or her age. Some shyness, fussiness or annoyance when being told what to do may be observed, but not to an atypical degree.",
                "response_text_ko": "예시: 아동은 낯선 사람과도 자연스럽게 대하며, 수줍음이나 까다로움이 보이더라도 전반적으로 정상적입니다.",
                "response_text_en": "Example: The child interacts naturally with others and shows only minimal shyness or fussiness."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 관계를 보입니다. 아동은 성인의 눈을 피하거나, 성인을 회피하거나, 상호작용을 강요당할 경우 까다롭게 반응할 수 있으며, 지나치게 수줍어하거나, 성인에게 일반적인 반응을 보이지 않거나, 또래 아동보다 부모에게 과도하게 집착할 수 있습니다.",
                "text_en": "(2) Mildly abnormal relationships. The child may avoid looking the adult in the eye, avoid the adult, or become fussy if interaction is forced; be excessively shy, less responsive than typical, or cling to parents more than most children of the same age.",
                "response_text_ko": "예시: 아동은 성인과의 눈맞춤을 피하거나 약간 과도하게 부모에게 집착합니다.",
                "response_text_en": "Example: The child may avoid eye contact with adults and cling to parents more than usual."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 관계를 보입니다. 아동은 때때로 냉담하거나 (성인에게 무관심한 듯 보임), 주의를 끌기 위해 지속적이고 강한 시도가 필요하며, 아동이 자발적으로 접촉을 시도하는 경우는 거의 없습니다.",
                "text_en": "(3) Moderately abnormal relationships. The child shows aloofness at times, requiring persistent and forceful attempts to get their attention; minimal contact is initiated by the child.",
                "response_text_ko": "예시: 아동은 때때로 주변에 무관심하며, 주의를 끌기 위해 많은 노력이 필요합니다.",
                "response_text_en": "Example: The child often appears aloof and requires persistent prompting to interact."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 관계를 보입니다. 아동은 지속적으로 냉담하거나 성인의 행동에 전혀 주의를 기울이지 않습니다. 성인과 접촉하거나 반응하는 일이 거의 없으며, 가장 강한 주의 환기도 효과가 거의 없습니다.",
                "text_en": "(4) Severely abnormal relationships. The child is constantly aloof or unaware of what the adult is doing, rarely initiating or responding to contact even with persistent attempts.",
                "response_text_ko": "예시: 아동은 주변 사람들과의 상호작용에 거의 관여하지 않습니다.",
                "response_text_en": "Example: The child rarely engages with others despite persistent efforts."
            }
        ]
    },
    {
        "id": 2,
        "question_ko": "모방",
        "question_en": "Imitation",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 적절한 모방을 보입니다. 아동은 자신의 기술 수준에 맞는 소리, 단어, 동작 등을 모방할 수 있습니다.",
                "text_en": "(1) Appropriate imitation. The child can imitate sounds, words, and movements appropriate for his or her skill level.",
                "response_text_ko": "예시: 아동은 자신의 발달 단계에 맞는 소리나 동작을 자연스럽게 모방합니다.",
                "response_text_en": "Example: The child naturally imitates sounds and movements appropriate for their developmental level."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 모방을 보입니다. 아동은 대부분의 경우 박수치기나 단순한 음성 모방과 같은 간단한 행동을 모방하지만, 때때로 자극이나 시간이 지난 후에야 모방합니다.",
                "text_en": "(2) Mildly abnormal imitation. The child imitates simple behaviors such as clapping or single verbal sounds most of the time; occasionally imitates only after prodding or a delay.",
                "response_text_ko": "예시: 아동은 간단한 동작은 모방하나, 때때로 지연되어 모방합니다.",
                "response_text_en": "Example: The child imitates simple actions, though sometimes only after a delay."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 모방을 보입니다. 아동은 일부만 모방하며, 성인의 많은 인내와 도움이 필요합니다. 자주 자극 후 시간이 지나서야 모방합니다.",
                "text_en": "(3) Moderately abnormal imitation. The child imitates only part of the time and requires substantial prompting and help from an adult; often imitates only after a delay.",
                "response_text_ko": "예시: 아동은 일부만 모방하여 성인의 많은 도움이 요구됩니다.",
                "response_text_en": "Example: The child imitates only partially and needs substantial prompting."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 모방을 보입니다. 아동은 자극과 도움에도 불구하고 소리, 단어, 동작 등을 거의 혹은 전혀 모방하지 않습니다.",
                "text_en": "(4) Severely abnormal imitation. The child rarely or never imitates sounds, words, or movements even with prodding and assistance.",
                "response_text_ko": "예시: 아동은 모방 반응이 거의 없으며, 성인의 시도에도 반응하지 않습니다.",
                "response_text_en": "Example: The child does not respond to imitation prompts even with help."
            }
        ]
    },
    {
        "id": 3,
        "question_ko": "정서 반응",
        "question_en": "Emotional Response",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 연령과 상황에 적절한 정서 반응을 보입니다. 아동은 표정, 자세, 태도의 변화를 통해 적절한 유형과 정도의 감정 반응을 보입니다.",
                "text_en": "(1) Age-appropriate and situation-appropriate responses. The child shows the appropriate type and degree of emotional response as indicated by changes in facial expression, posture, and manner.",
                "response_text_ko": "예시: 아동은 상황에 맞는 감정을 자연스럽게 표현합니다.",
                "response_text_en": "Example: The child expresses emotions appropriately for the situation."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 정서 반응을 보입니다. 아동은 때때로 다소 부적절한 유형이나 강도의 감정 반응을 나타내며, 반응이 주변 사물이나 사건과 무관할 수 있습니다.",
                "text_en": "(2) Mildly abnormal emotional responses. The child occasionally displays a somewhat inappropriate type or degree of emotional response; reactions may be unrelated to surrounding events.",
                "response_text_ko": "예시: 아동은 때로 상황과 맞지 않는 감정 표현을 보입니다.",
                "response_text_en": "Example: The child sometimes shows emotional responses that are slightly out of context."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 정서 반응을 보입니다. 아동은 확실히 부적절한 유형 및/또는 정도의 감정 반응을 보입니다. 상황과 무관하게 표정을 찡그리거나, 웃거나, 몸을 뻣뻣하게 만드는 등 억제되거나 과도한 반응을 보일 수 있습니다.",
                "text_en": "(3) Moderately abnormal emotional responses. The child shows definite signs of inappropriate type and/or degree of emotional response; reactions may be inhibited or excessive regardless of context.",
                "response_text_ko": "예시: 아동은 상황과 상관없이 과도하거나 억제된 감정 표현을 보입니다.",
                "response_text_en": "Example: The child exhibits emotional responses that are either too constrained or too exaggerated, regardless of context."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 정서 반응을 보입니다. 상황에 적절한 반응을 거의 보이지 않으며, 특정 기분에 빠지면 그 기분을 바꾸는 것이 매우 어렵습니다. 또는, 아무런 변화도 없는데 전혀 다른 감정을 갑자기 나타내기도 합니다.",
                "text_en": "(4) Severely abnormal emotional responses. Responses are seldom appropriate to the situation; once in a certain mood, it is very difficult for the child to change it. Conversely, the child may display wildly different emotions without any apparent change in situation.",
                "response_text_ko": "예시: 아동은 특정 기분 상태에서 벗어나기 어려워하며 극단적인 감정 변화가 보입니다.",
                "response_text_en": "Example: The child remains stuck in a mood and shows severe, inappropriate emotional shifts."
            }
        ]
    },
    {
        "id": 4,
        "question_ko": "신체 사용",
        "question_en": "Body Use",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 연령에 적절한 신체 사용을 보입니다. 아동은 또래의 정상 아동처럼 쉽게 움직이고 민첩하며 협응이 잘 이루어집니다.",
                "text_en": "(1) Age appropriate body use. The child moves with the ease, agility, and coordination of a normal child of the same age.",
                "response_text_ko": "예시: 아동은 자유롭고 조화롭게 움직입니다.",
                "response_text_en": "Example: The child moves with ease and shows good coordination."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 신체 사용을 보입니다. 약간의 어색함, 반복 동작, 협응 부족 또는 드물게 더 비정상적인 움직임이 나타날 수 있습니다.",
                "text_en": "(2) Mildly abnormal body use. Some minor peculiarities such as clumsiness, repetitive movements, or poor coordination may be observed.",
                "response_text_ko": "예시: 아동은 다소 어색한 움직임이나 반복 동작을 보일 수 있습니다.",
                "response_text_en": "Example: The child may occasionally display slight awkwardness or repetitive movements."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 신체 사용을 보입니다. 또래 아동에게서 보기 힘든 이상한 손가락 움직임, 특이한 자세, 응시, 몸을 만지거나 뜯는 행동, 자해, 흔들기, 빙글빙글 돌기, 발끝으로 걷기 등이 포함될 수 있습니다.",
                "text_en": "(3) Moderately abnormal body use. Behaviors clearly unusual for a child of this age may include peculiar finger movements, odd posturing, staring, body picking, self-directed aggression, rocking, spinning, or toe walking.",
                "response_text_ko": "예시: 아동은 비정상적인 손가락 움직임이나 자세 등으로 주의가 필요합니다.",
                "response_text_en": "Example: The child shows unusual finger movements or postures that require attention."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 신체 사용을 보입니다. 위에서 언급한 행동들이 강도 높고 자주 나타납니다. 이러한 행동은 제지하려 해도 계속되며, 다른 활동으로 아동을 유도해도 쉽게 중단되지 않습니다.",
                "text_en": "(4) Severely abnormal body use. Intense or frequent occurrences of the above behaviors that persist despite attempts to discourage them or direct the child to other activities.",
                "response_text_ko": "예시: 아동은 극단적이고 지속적인 비정상적 움직임을 보입니다.",
                "response_text_en": "Example: The child exhibits severe, persistent abnormal movements that are hard to interrupt."
            }
        ]
    },
    {
        "id": 5,
        "question_ko": "사물 사용",
        "question_en": "Object Use",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 장난감과 기타 사물에 대한 사용과 관심이 적절합니다. 아동은 자신의 기술 수준에 맞는 장난감과 사물에 정상적인 관심을 보이며 이를 적절한 방식으로 사용합니다.",
                "text_en": "(1) Appropriate use of, and interest in, toys and other objects. The child shows normal interest in and uses toys appropriate for his or her skill level.",
                "response_text_ko": "예시: 아동은 장난감을 정상적으로 사용하고 관심을 보입니다.",
                "response_text_en": "Example: The child uses toys appropriately and shows normal interest."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 부적절한 사물 사용과 관심을 보입니다. 아동은 장난감에 비정상적인 관심을 보이거나, 장난감을 부적절하고 유아적인 방식(예: 장난감을 두드리거나 빨기)으로 사용할 수 있습니다.",
                "text_en": "(2) Mildly inappropriate use of, and interest in, toys and other objects. The child may show atypical interest in a toy or play with it in an inappropriate, childish way (e.g. banging or sucking on it).",
                "response_text_ko": "예시: 아동은 장난감을 부적절하게 다루거나 지나치게 집착할 수 있습니다.",
                "response_text_en": "Example: The child may handle toys in an overly infantile or atypical manner."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 부적절한 사물 사용과 관심을 보입니다. 아동은 장난감이나 사물에 거의 관심을 보이지 않거나, 특정 사물이나 장난감을 이상한 방식으로 사용하는 데 집착할 수 있습니다. 예를 들어, 사물의 사소한 부분에 집중하거나, 빛 반사에 매료되거나, 특정 부분을 반복적으로 움직이거나, 그 사물만 가지고 놀 수 있습니다.",
                "text_en": "(3) Moderately inappropriate use of, and interest in, toys and other objects. The child may show little interest or be fixated on using an object in an unusual way, such as focusing on an insignificant part, being fascinated by reflections, or repeatedly moving a part of it.",
                "response_text_ko": "예시: 아동은 특정 사물에 집착하여 비정상적인 방식으로 놀 수 있습니다.",
                "response_text_en": "Example: The child fixates on a specific aspect of a toy and plays with it in an unusual manner."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 부적절한 사물 사용과 관심을 보입니다. 위와 같은 행동이 훨씬 더 자주, 강하게 나타납니다. 아동이 이러한 부적절한 활동에 몰두하면 주의가 산만해지기 어려울 정도입니다.",
                "text_en": "(4) Severely inappropriate use of, and interest in, toys and other objects. The behaviors occur with greater frequency and intensity, making it difficult to distract the child from such activity.",
                "response_text_ko": "예시: 아동은 사물에 지나치게 몰입하여 다른 활동에 관심을 보이지 않습니다.",
                "response_text_en": "Example: The child becomes extremely fixated on objects, making redirection very difficult."
            }
        ]
    },
    {
        "id": 6,
        "question_ko": "변화에 대한 적응",
        "question_en": "Adaptation to Change",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 변화에 대해 연령에 적절하게 반응합니다. 아동은 일상의 변화에 대해 알아차리거나 언급할 수 있으나, 과도한 불편함 없이 이를 수용합니다.",
                "text_en": "(1) Age appropriate responses to change. The child notices or comments on changes in routines but accepts them without undue distress.",
                "response_text_ko": "예시: 아동은 변화에 대해 비교적 수용적입니다.",
                "response_text_en": "Example: The child accepts changes in routine without significant distress."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 변화 반응을 보입니다. 성인이 과제를 바꾸려 하면 아동은 같은 활동이나 동일한 자료를 계속 사용하려고 할 수 있습니다.",
                "text_en": "(2) Mildly abnormal responses to change. When an adult tries to change tasks, the child may continue the same activity or use the same materials.",
                "response_text_ko": "예시: 아동은 기존 활동에 집착하여 변화에 저항합니다.",
                "response_text_en": "Example: The child tends to stick to the same activity and shows resistance to change."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 변화 반응을 보입니다. 아동은 일상적 루틴의 변화에 강하게 저항하며, 이전 활동을 계속하려 하고 주의를 돌리기 어렵습니다. 루틴이 변경되면 화를 내거나 불행해할 수 있습니다.",
                "text_en": "(3) Moderately abnormal responses to change. The child strongly resists changes in routine, trying to continue the old activity and is difficult to distract; may become angry or upset when routines change.",
                "response_text_ko": "예시: 아동은 루틴의 변화에 강한 저항과 불만을 보입니다.",
                "response_text_en": "Example: The child exhibits notable resistance and frustration when routines change."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 변화 반응을 보입니다. 아동은 변화에 대해 심각한 반응을 보입니다. 변화가 강제로 이루어지면, 아동은 매우 화를 내거나 협조하지 않으며, 분노 발작으로 반응할 수 있습니다.",
                "text_en": "(4) Severely abnormal responses to change. The child shows severe reactions; when change is forced, may become extremely angry, uncooperative, or have tantrums.",
                "response_text_ko": "예시: 아동은 강제된 변화에 대해 극단적인 분노와 협조 어려움을 보입니다.",
                "response_text_en": "Example: The child reacts with severe tantrums and uncooperative behavior when forced to change activities."
            }
        ]
    },
    {
        "id": 7,
        "question_ko": "시각 반응",
        "question_en": "Visual Response",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 아동의 시각적 행동은 연령에 적절하며 정상적입니다. 아동은 새로운 사물을 탐색할 때 시각을 다른 감각과 함께 사용합니다.",
                "text_en": "(1) The child’s visual behavior is normal and age appropriate; vision is used with other senses to explore objects.",
                "response_text_ko": "예시: 아동은 시각적 탐색을 통해 사물을 잘 관찰합니다.",
                "response_text_en": "Example: The child appropriately uses vision to explore new objects."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 시각 반응을 보입니다. 아동은 때때로 사물을 보기 위해 상기시켜야 하며, 또래보다 거울이나 빛에 더 관심을 보일 수 있고, 때로는 멍하니 허공을 바라보거나 사람의 눈을 피할 수 있습니다.",
                "text_en": "(2) Mildly abnormal visual response. The child sometimes needs reminding to look at objects and may be more interested in mirrors or light, occasionally staring off into space or avoiding eye contact.",
                "response_text_ko": "예시: 아동은 때때로 시각적 주의를 요하며, 멍하니 바라보는 경향이 있습니다.",
                "response_text_en": "Example: The child sometimes needs reminders and may stare off into space."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 시각 반응을 보입니다. 아동은 자신이 하고 있는 일을 보도록 자주 상기시켜야 합니다. 그는 멍하니 허공을 응시하거나, 사람의 눈을 피하거나, 사물을 이상한 각도로 보거나, 매우 가까이 들여다볼 수 있습니다.",
                "text_en": "(3) Moderately abnormal visual response. The child frequently needs to be reminded to look at what they are doing; may stare into space, avoid eye contact, view objects from unusual angles, or hold objects very close.",
                "response_text_ko": "예시: 아동은 지속적으로 시선을 돌려야 하며, 이상한 각도로 사물을 바라봅니다.",
                "response_text_en": "Example: The child frequently requires prompting and may view objects from odd angles."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 시각 반응을 보입니다. 아동은 지속적으로 사람이나 특정 사물을 보지 않으려 하며, 위에서 설명된 극단적인 시각 이상 행동을 나타낼 수 있습니다.",
                "text_en": "(4) Severely abnormal visual response. The child consistently avoids looking at people or specific objects and may show extreme visual peculiarities.",
                "response_text_ko": "예시: 아동은 눈맞춤이나 특정 사물에 대한 시각적 반응을 거의 보이지 않습니다.",
                "response_text_en": "Example: The child almost completely avoids visual engagement with people or objects."
            }
        ]
    },
    {
        "id": 8,
        "question_ko": "청각 반응",
        "question_en": "Listening Response",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 아동의 청각적 반응은 연령에 적절하고 정상적입니다. 청각은 다른 감각과 함께 사용됩니다.",
                "text_en": "(1) Age appropriate listening responses. The child’s listening behavior is normal and appropriate for age; listening is used with other senses.",
                "response_text_ko": "예시: 아동은 정상적으로 소리에 반응합니다.",
                "response_text_en": "Example: The child listens and responds appropriately."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 청각 반응을 보입니다. 일부 소리에 반응이 없거나 과도하게 반응할 수 있으며, 반응이 지연되거나 반복된 소리 자극이 있어야 주의를 기울입니다. 주변 소리에 쉽게 산만해질 수 있습니다.",
                "text_en": "(2) Mildly abnormal listening responses. There may be some lack of response or mild overreaction; responses may be delayed and require repetition, with the child easily distracted by background noise.",
                "response_text_ko": "예시: 아동은 소리에 대한 반응이 다소 느리거나 과장될 수 있습니다.",
                "response_text_en": "Example: The child may show delayed or slightly exaggerated responses to sound."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 청각 반응을 보입니다. 아동의 소리에 대한 반응은 일정하지 않으며, 처음 몇 번은 무시하다가 나중에 반응합니다. 일상적인 소리에도 깜짝 놀라거나 귀를 막을 수 있습니다.",
                "text_en": "(3) Moderately abnormal listening responses. The child’s responses are inconsistent – often ignoring initial sounds and reacting later; may be startled or cover ears at everyday sounds.",
                "response_text_ko": "예시: 아동은 소리에 대한 반응이 변동성이 있으며, 가끔 깜짝 놀랍니다.",
                "response_text_en": "Example: The child's response to sound is inconsistent, often ignoring initial sounds and reacting later."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 청각 반응을 보입니다. 아동은 특정 소리의 종류와 무관하게 청각 자극에 과도하거나 지나치게 둔감하게 반응합니다.",
                "text_en": "(4) Severely abnormal listening responses. The child overreacts or underreacts to sounds to an extreme degree, regardless of the type of sound.",
                "response_text_ko": "예시: 아동은 소리에 대해 극단적으로 과민하거나 둔감하게 반응합니다.",
                "response_text_en": "Example: The child demonstrates an extreme overreaction or underreaction to auditory stimuli."
            }
        ]
    }
]

# PART 2 : questions 9 ~ 15
cars_mapping_part2 = [
    {
        "id": 9,
        "question_ko": "미각, 후각, 촉각 반응 및 사용",
        "question_en": "Taste, Smell, and Touch Response and Use",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 미각, 후각, 촉각에 대한 사용 및 반응이 정상적입니다. 아동은 연령에 적절한 방식으로 새로운 사물을 주로 만지거나 보면서 탐색합니다. 필요할 경우 맛보거나 냄새를 맡기도 합니다. 일상적인 가벼운 통증에 대해서는 불편함을 표현하지만 과도하게 반응하지 않습니다.",
                "text_en": "(1) Normal use of, and response to, taste, smell, and touch. The child explores new objects in an age appropriate manner by feeling or looking; may taste or smell when appropriate. Reacts to minor pain with discomfort but not overreaction.",
                "response_text_ko": "예시: 아동은 감각을 활용하여 사물을 탐색하고, 약한 통증에는 정상적으로 반응합니다.",
                "response_text_en": "Example: The child uses their senses to explore objects and responds appropriately to mild pain."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 사용 및 반응을 보입니다. 아동은 사물을 입에 넣는 행동을 지속할 수 있고, 먹을 수 없는 물건을 맛보거나 냄새 맡을 수 있으며, 일반 아동이라면 단순한 불편함 정도로 반응할 사소한 통증에 무반응하거나 과도하게 반응할 수 있습니다.",
                "text_en": "(2) Mildly abnormal use of, and responses to, taste, smell, and touch. The child may persist in putting objects in the mouth, may taste or smell inedible objects, and may underreact or overreact to minor pain.",
                "response_text_ko": "예시: 아동은 사물을 입에 넣거나 냄새 맡으며, 통증 반응이 다소 비정상적입니다.",
                "response_text_en": "Example: The child frequently puts objects in their mouth or smells things, showing an abnormal response to minor pain."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 사용 및 반응을 보입니다. 아동은 사물이나 사람을 만지거나 냄새 맡거나 맛보는 데 중간 정도로 집착할 수 있으며, 감각 자극에 지나치게 많이 또는 적게 반응할 수 있습니다.",
                "text_en": "(3) Moderately abnormal use of, and responses to, taste, smell, and touch. The child may show moderate preoccupation with touching, smelling, or tasting, reacting either too much or too little.",
                "response_text_ko": "예시: 아동은 감각적 자극에 대해 중간 정도 집착하며 반응이 과하거나 부족할 수 있습니다.",
                "response_text_en": "Example: The child shows moderate preoccupation with sensory stimuli, reacting either excessively or insufficiently."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 사용 및 반응을 보입니다. 아동은 사물의 정상적인 탐색이나 사용보다는 감각 자체에 대한 자극을 위해 사물을 만지거나 냄새 맡거나 맛보는 데 몰두합니다. 아동은 통증을 완전히 무시하거나 아주 미세한 불편에도 매우 강하게 반응할 수 있습니다.",
                "text_en": "(4) Severely abnormal use of, and responses to, taste, smell, and touch. The child is preoccupied with the sensory stimulation itself, may completely ignore pain or react extremely to slight discomfort.",
                "response_text_ko": "예시: 아동은 감각 자극에 지나치게 몰입하여, 통증에 극도로 민감하거나 전혀 반응하지 않습니다.",
                "response_text_en": "Example: The child is overly fixated on sensory input and reacts either extremely or not at all to pain."
            }
        ]
    },
    {
        "id": 10,
        "question_ko": "두려움 또는 불안",
        "question_en": "Fear or Nervousness",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 정상적인 두려움이나 불안을 보입니다. 아동의 행동은 상황과 나이에 모두 적절합니다.",
                "text_en": "(1) Normal fear or nervousness. The child’s behavior is appropriate for both the situation and age.",
                "response_text_ko": "예시: 아동은 상황에 맞춰 적절한 두려움과 불안을 보입니다.",
                "response_text_en": "Example: The child displays appropriate fear and nervousness relative to the situation."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 두려움이나 불안을 보입니다. 아동은 같은 연령대의 정상 아동들과 비교했을 때 상황에 대해 지나치거나 부족한 두려움이나 불안을 간헐적으로 보일 수 있습니다.",
                "text_en": "(2) Mildly abnormal fear or nervousness. The child occasionally shows too much or too little fear compared to peers in similar situations.",
                "response_text_ko": "예시: 아동은 때때로 과도하거나 부족한 두려움 반응을 보입니다.",
                "response_text_en": "Example: The child occasionally exhibits an irregular degree of fear or nervousness."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 두려움이나 불안을 보입니다. 아동은 비슷한 상황에서 일반적인 아동보다 훨씬 더 많거나 적은 두려움을 보입니다. 이는 심지어 연령이 더 많거나 적은 아동과 비교해도 눈에 띄는 수준입니다.",
                "text_en": "(3) Moderately abnormal fear or nervousness. The child shows significantly more or less fear than typical children in similar situations, noticeable even when compared to children of different ages.",
                "response_text_ko": "예시: 아동은 동료에 비해 눈에 띄게 두려움 정도가 다릅니다.",
                "response_text_en": "Example: The child exhibits noticeably more or less fear compared to peers."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 두려움이나 불안을 보입니다. 무해한 사건이나 사물에 대해 반복적인 경험 후에도 두려움을 지속하며, 진정시키거나 위로하는 것이 매우 어렵습니다. 반대로, 또래 아동이라면 경계할 만한 위험 요소에 대해 무관심할 수 있습니다.",
                "text_en": "(4) Severely abnormal fear or nervousness. The child continues to fear even harmless events or objects and is extremely difficult to soothe; alternatively, may show inappropriate indifference to hazards.",
                "response_text_ko": "예시: 아동은 지속적이고 과도한 두려움을 보여 위로가 어렵습니다.",
                "response_text_en": "Example: The child exhibits persistent, severe fear that is hard to soothe."
            }
        ]
    },
    {
        "id": 11,
        "question_ko": "언어적 의사소통",
        "question_en": "Verbal Communication",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 언어적 의사소통이 연령과 상황에 적절하며 정상적입니다.",
                "text_en": "(1) Normal verbal communication, age and situation appropriate.",
                "response_text_ko": "예시: 아동은 정상적인 언어 표현을 구사합니다.",
                "response_text_en": "Example: The child communicates verbally in an age-appropriate manner."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 언어적 의사소통을 보입니다. 전반적으로 언어 발달이 지연되어 있으며, 대부분의 언어는 의미가 있으나 때때로 반향어(echolalia)나 인칭대명사 혼용이 나타날 수 있습니다. 드물게 특이한 단어나 은어(jargon)를 사용할 수도 있습니다.",
                "text_en": "(2) Mildly abnormal verbal communication. Speech shows overall retardation; most speech is meaningful, although occasional echolalia or pronoun reversal (or even jargon) may occur.",
                "response_text_ko": "예시: 아동은 때때로 언어 표현에 경미한 지연이나 혼동이 있습니다.",
                "response_text_en": "Example: The child sometimes displays minor speech delays or confusions such as echolalia."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 언어적 의사소통을 보입니다. 말이 없는 경우도 있으며, 존재하는 경우에도 의미 있는 의사소통과 특이한 언어(예: 은어, 반향어, 인칭대명사 혼용 등)가 혼합되어 있습니다. 의미 있는 말에서도 지나친 질문 반복이나 특정 주제에의 집착과 같은 이상이 나타날 수 있습니다.",
                "text_en": "(3) Moderately abnormal verbal communication. Speech may be absent, and when present, may be a mix of meaningful communication and peculiar language (jargon, echolalia, pronoun reversal), with excessive questioning or preoccupation with a topic.",
                "response_text_ko": "예시: 아동은 언어가 거의 없거나 일반적인 의사소통에 비정상적인 요소가 섞여 있습니다.",
                "response_text_en": "Example: The child may be largely nonverbal or show a blend of typical and unusual speech patterns."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 언어적 의사소통을 보입니다. 의미 있는 언어를 사용하지 않으며, 유아적인 비명, 이상하거나 동물적인 소리, 말처럼 들리는 복잡한 잡음 또는 알아들을 수 있는 단어나 구절을 지속적으로 이상한 방식으로 사용할 수 있습니다.",
                "text_en": "(4) Severely abnormal verbal communication. Meaningful speech is not used; the child may produce infantile squeals, weird or animal-like sounds, or complex noises approximating speech in a bizarre manner.",
                "response_text_ko": "예시: 아동은 의미 있는 단어 없이 비정상적인 소리나 잡음을 지속적으로 냅니다.",
                "response_text_en": "Example: The child consistently produces non-meaningful sounds and lacks normal verbal communication."
            }
        ]
    },
    {
        "id": 12,
        "question_ko": "비언어적 의사소통",
        "question_en": "Nonverbal Communication",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 비언어적 의사소통이 연령과 상황에 적절하며 정상적입니다.",
                "text_en": "(1) Normal use of nonverbal communication, age and situation appropriate.",
                "response_text_ko": "예시: 아동은 정상적인 비언어적 표현을 사용합니다.",
                "response_text_en": "Example: The child uses normal nonverbal cues."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 비언어적 의사소통을 보입니다. 미숙한 비언어적 표현을 사용하며, 또래 아동들이 명확히 가리키거나 몸짓으로 자신의 욕구를 전달할 상황에서도 단지 막연히 가리키거나 손만 뻗는 등 부정확한 표현을 사용할 수 있습니다.",
                "text_en": "(2) Mildly abnormal use of nonverbal communication. Uses immature nonverbal expression; may only point vaguely or reach without clarity when peers would indicate more precisely.",
                "response_text_ko": "예시: 아동은 때때로 모호한 손짓이나 제스처만을 사용합니다.",
                "response_text_en": "Example: The child occasionally uses vague gestures to communicate needs."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 비언어적 의사소통을 보입니다. 아동은 일반적으로 비언어적으로 자신의 욕구나 의도를 표현하지 못하며, 다른 사람의 비언어적 표현도 이해하지 못합니다.",
                "text_en": "(3) Moderately abnormal use of nonverbal communication. The child generally fails to express needs nonverbally and cannot understand others’ nonverbal cues.",
                "response_text_ko": "예시: 아동은 비언어적 의사소통에서 어려움을 겪습니다.",
                "response_text_en": "Example: The child struggles to both express and understand nonverbal cues."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 비언어적 의사소통을 보입니다. 아동은 의미가 없는 이상하거나 특이한 몸짓만을 사용하며, 타인의 얼굴 표정이나 몸짓에 담긴 의미에 전혀 주의를 기울이지 않습니다.",
                "text_en": "(4) Severely abnormal use of nonverbal communication. The child uses only bizarre, meaningless gestures and shows no awareness of the meaning of others’ facial expressions or gestures.",
                "response_text_ko": "예시: 아동은 전혀 이해할 수 없는 비정상적인 몸짓만을 사용합니다.",
                "response_text_en": "Example: The child uses only bizarre, meaningless gestures."
            }
        ]
    },
    {
        "id": 13,
        "question_ko": "활동 수준",
        "question_en": "Activity Level",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 연령과 상황에 적절한 정상적인 활동 수준을 보입니다. 아동은 비슷한 상황에 있는 또래 아동보다 지나치게 활동적이거나 활동이 부족하지 않습니다.",
                "text_en": "(1) Normal activity level for age and circumstances. The child is neither overly active nor inactive compared to peers.",
                "response_text_ko": "예시: 아동은 정상적인 활동성을 유지합니다.",
                "response_text_en": "Example: The child maintains a normal level of activity."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 활동 수준을 보입니다. 아동은 다소 안절부절 못하거나 반대로 약간 게으르고 느릿느릿 움직이는 모습을 보일 수 있으며, 활동 수준은 아동의 수행에 약간의 영향을 미칠 수 있습니다.",
                "text_en": "(2) Mildly abnormal activity level. The child may be mildly restless or somewhat slow-moving, with activity levels slightly interfering with performance.",
                "response_text_ko": "예시: 아동은 때때로 약간 안절부절하거나 느리게 움직입니다.",
                "response_text_en": "Example: The child sometimes appears slightly restless or sluggish."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 활동 수준을 보입니다. 아동은 매우 활동적이며 제어하기 어렵습니다. 에너지가 넘치거나 밤에 쉽게 잠들지 못할 수 있습니다. 반대로, 매우 무기력하여 움직이기 위해 많은 자극이 필요할 수도 있습니다.",
                "text_en": "(3) Moderately abnormal activity level. The child may be very active and hard to restrain – having boundless energy or difficulty sleeping; alternatively, may be markedly lethargic requiring much prompting.",
                "response_text_ko": "예시: 아동은 과도하게 활동적이거나 또는 무기력한 모습을 보입니다.",
                "response_text_en": "Example: The child may display excessive energy or noticeable lethargy."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 활동 수준을 보입니다. 아동은 극단적인 활동성 또는 무기력함을 보이며, 이 두 상태를 오가기도 합니다.",
                "text_en": "(4) Severely abnormal activity level. The child exhibits extremes of activity or inactivity, sometimes shifting between the two.",
                "response_text_ko": "예시: 아동은 극단적으로 활동적이거나 무기력하여 조절이 어렵습니다.",
                "response_text_en": "Example: The child shows extreme fluctuations in activity levels that are difficult to manage."
            }
        ]
    },
    {
        "id": 14,
        "question_ko": "지적 반응의 수준과 일관성",
        "question_en": "Level and Consistency of Intellectual Response",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 지능은 정상이며 다양한 영역에서 비교적 일관성을 보입니다. 아동은 또래의 일반적인 아동들과 비슷한 수준의 지능을 보이며, 특이한 지적 기술이나 문제를 나타내지 않습니다.",
                "text_en": "(1) Intelligence is normal and reasonably consistent across various areas. The child demonstrates intelligence comparable to typical peers.",
                "response_text_ko": "예시: 아동은 정상적인 지적 능력을 보입니다.",
                "response_text_en": "Example: The child demonstrates normal intellectual functioning."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미하게 비정상적인 지적 기능을 보입니다. 아동은 또래 아동보다 똑똑하지 않으며, 모든 영역에서 기술 수준이 고르게 낮습니다.",
                "text_en": "(2) Mildly abnormal intellectual functioning. The child is not as smart as typical children; skills appear consistently lower across areas.",
                "response_text_ko": "예시: 아동은 전반적으로 또래보다 다소 낮은 지적 능력을 보입니다.",
                "response_text_en": "Example: The child shows mildly reduced intellectual functioning compared to peers."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도로 비정상적인 지적 기능을 보입니다. 전반적으로 아동은 또래보다 지능이 낮지만, 일부 지적 영역에서는 거의 정상적으로 기능할 수도 있습니다.",
                "text_en": "(3) Moderately abnormal intellectual functioning. Overall, the child is less intelligent than typical peers, though may function nearly normally in some areas.",
                "response_text_ko": "예시: 아동은 일부 영역에서는 정상적이나 전반적으로 낮은 지능을 보입니다.",
                "response_text_en": "Example: The child exhibits generally lower intelligence with some near-normal areas."
            },
            {
                "score": 4,
                "text_ko": "(4) 심하게 비정상적인 지적 기능을 보입니다. 아동은 일반적으로 또래보다 지능이 낮지만, 한두 영역에서는 오히려 또래보다 더 높은 기능을 보일 수 있습니다.",
                "text_en": "(4) Severely abnormal intellectual functioning. The child generally demonstrates lower intelligence than peers, yet may excel in one or more specific areas.",
                "response_text_ko": "예시: 아동은 특정 영역에서 뛰어난 능력을 보이나, 전반적으로는 낮은 지능을 나타냅니다.",
                "response_text_en": "Example: The child may excel in a specific area despite overall reduced intellectual functioning."
            }
        ]
    },
    {
        "id": 15,
        "question_ko": "종합 인상",
        "question_en": "General Impressions",
        "description_ko": "",
        "description_en": "",
        "options": [
            {
                "score": 1,
                "text_ko": "(1) 자폐가 아님: 아동은 자폐의 특징적인 증상을 전혀 보이지 않습니다.",
                "text_en": "(1) No Autism: The child shows none of the symptoms characteristic of autism.",
                "response_text_ko": "예시: 아동은 자폐 증상이 전혀 관찰되지 않습니다.",
                "response_text_en": "Example: The child does not exhibit any autistic symptoms."
            },
            {
                "score": 2,
                "text_ko": "(2) 경미한 자폐: 아동은 몇 가지 증상만을 보이거나 경미한 수준의 자폐 특성을 보입니다.",
                "text_en": "(2) Mild Autism. The child shows only a few symptoms or only mild autistic features.",
                "response_text_ko": "예시: 아동은 경미한 자폐 특성을 보입니다.",
                "response_text_en": "Example: The child displays only a few mild autistic features."
            },
            {
                "score": 3,
                "text_ko": "(3) 중등도 자폐: 아동은 여러 개의 자폐 증상을 보이며, 그 정도도 중간 수준입니다.",
                "text_en": "(3) Moderate autism. The child shows several symptoms or a moderate degree of autism.",
                "response_text_ko": "예시: 아동은 여러 자폐 증상을 보이며 중간 정도입니다.",
                "response_text_en": "Example: The child exhibits several autistic symptoms at a moderate level."
            },
            {
                "score": 4,
                "text_ko": "(4) 심한 자폐: 아동은 많은 자폐 증상을 보이거나 극단적인 수준의 자폐 특성을 보입니다.",
                "text_en": "(4) Severe autism. The child shows many symptoms or an extreme degree of autism.",
                "response_text_ko": "예시: 아동은 자폐 증상이 다수 관찰되며 심한 상태입니다.",
                "response_text_en": "Example: The child displays numerous and severe autistic symptoms."
            }
        ]
    }
]

# Combine both parts into one assessment mapping list
cars_mapping = cars_mapping_part1 + cars_mapping_part2

# ----------------------------- Function Definitions -----------------------------
def display_questions(cars_mapping):
    st.write("아래 문항에 모두 응답해 주세요:")
    for i, q in enumerate(cars_mapping):
        st.write(f"{i+1}. {q['question_ko']}")
        options_ko = [opt["text_ko"] for opt in q["options"]]
        st.selectbox("답변 선택", options_ko, key=f"q_{i}")

def calculate_results(cars_mapping):
    total_score = 0
    output = "CARS Assessment\n\n"
    for i, q in enumerate(cars_mapping):
        options_ko = [opt["text_ko"] for opt in q["options"]]
        selected_text = st.session_state.get(f"q_{i}", options_ko[0])
        try:
            selected_index = options_ko.index(selected_text)
        except ValueError:
            selected_index = 0
        selected_option = q["options"][selected_index]
        total_score += selected_option["score"]
        output += f"{i+1}. {q['question_en']}\n"
        # 영어 응답 문장은 이미 점수가 포함되어 있으므로, 별도 점수 출력 없이 text_en만 출력합니다.
        output += f"   {selected_option['text_en']}\n\n"
    output += f"Total Score: {total_score}\n"
    if total_score < 30:
        interpretation = "WNL"
    elif 30 <= total_score <= 36:
        interpretation = "Mild to Moderate Autism"
    else:
        interpretation = "Severe Autism"
    output += f"Interpretation: {interpretation}"
    return output

def reset_state():
    st.session_state.submitted = False
    for key in list(st.session_state.keys()):
        if key.startswith("q_"):
            del st.session_state[key]

# ----------------------------- Streamlit App -----------------------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("CARS Evaluation Tool")

if not st.session_state.submitted:
    display_questions(cars_mapping)
    if st.button("제출"):
        st.session_state.submitted = True
else:
    result = calculate_results(cars_mapping)
    st.code(result)
    if st.button("다시 평가하기"):
        reset_state()
