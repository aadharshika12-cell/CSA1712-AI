
disease(diabetes).
disease(hypertension).
disease(obesity).

diet(diabetes, 'Balanced meals with controlled carbohydrates').
diet(hypertension, 'Lower-sodium foods and vegetables').
diet(obesity, 'Balanced portions and nutrient-rich foods').

suggest_diet(Disease) :-
    diet(Disease, Advice),
    write('General diet suggestion: '),
    write(Advice), nl.
