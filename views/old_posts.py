from flask import Blueprint, render_template

old_posts = Blueprint("old-posts", __name__)

@old_posts.route('how-cold-makes-you-stronger.html')
def how_cold_makes_you_stronger():
   return render_template('posts/how-cold-makes-you-stronger.html')

@old_posts.route('how-to-lose-weight-with-cold.html')
def how_to_lose_weight_with_cold():
   return render_template('posts/how-to-lose-weight-with-cold.html')

@old_posts.route('sport-and-cold-what-to-cool.html')
def sport_and_cold_what_to_cool():
   return render_template('posts/sport-and-cold-what-to-cool.html')

@old_posts.route('light-brightness-recommendations.html')
def light_brightness_recommendations():
   return render_template('posts/light-brightness-recommendations.html')

@old_posts.route('cortisol-stress-hormone.html')
def cortisol_stress_hormone():
   return render_template('posts/cortisol-stress-hormone.html')

@old_posts.route('visible-light-spectrum-artificial.html')
def visible_light_spectrum_artificial():
   return render_template('posts/visible-light-spectrum-artificial.html')

@old_posts.route('which-useful-compounds-microbiom-makes-for-us.html')
def which_useful_compounds_microbiom_makes_for_us():
   return render_template('posts/which-useful-compounds-microbiom-makes-for-us.html')

@old_posts.route('mimicking-fasting.html')
def mimicking_fasting():
   return render_template('posts/mimicking-fasting.html')

@old_posts.route('brown-fat.html')
def brown_fat():
   return render_template('posts/brown-fat.html')

@old_posts.route('caffeine-sleep.html')
def caffeine_sleep():
   return render_template('posts/caffeine-sleep.html')

@old_posts.route('metabolism-and-sleep.html')
def metabolism_and_sleep():
   return render_template('posts/metabolism-and-sleep.html')

@old_posts.route('mitochondria-overload.html')
def mitochondria_overload():
   return render_template('posts/mitochondria-overload.html')

@old_posts.route('what-destroying-microbiome-i.html')
def what_destroying_microbiome_i():
   return render_template('posts/what-destroying-microbiome-i.html')

@old_posts.route('how-microbs-manipulate-with-our-food-preferences.html')
def how_microbs_manipulate_with_our_food_preferences():
   return render_template('posts/how-microbs-manipulate-with-our-food-preferences.html')

@old_posts.route('fasting-variations.html')
def fasting_variations():
   return render_template('posts/fasting-variations.html')

@old_posts.route('microbiome-in-general.html')
def microbiome_in_general():
   return render_template('posts/microbiome-in-general.html')

@old_posts.route('three-colors-of-fat.html')
def three_colors_of_fat():
   return render_template('posts/three-colors-of-fat.html')

@old_posts.route('how-mental-health-depends-on-microbiome.html')
def how_mental_health_depends_on_microbiome():
   return render_template('posts/how-mental-health-depends-on-microbiome.html')

@old_posts.route('night-life-problems.html')
def night_life_problems():
   return render_template('posts/night-life-problems.html')

@old_posts.route('fasting-nuances-v-ending-fast.html')
def fasting_nuances_v_ending_fast():
   return render_template('posts/fasting-nuances-v-ending-fast.html')

@old_posts.route('sleepy-immune-system.html')
def sleepy_immune_system():
   return render_template('posts/sleepy-immune-system.html')

@old_posts.route('circadiam-rhytms-and-scn.html')
def circadiam_rhytms_and_scn():
   return render_template('posts/circadiam-rhytms-and-scn.html')

@old_posts.route('how-our-immune-system-depends-on-microbs.html')
def how_our_immune_system_depends_on_microbs():
   return render_template('posts/how-our-immune-system-depends-on-microbs.html')

@old_posts.route('visible-light-spectrum-natural.html')
def visible_light_spectrum_natural():
   return render_template('posts/visible-light-spectrum-natural.html')

@old_posts.route('night-life-recommendations.html')
def night_life_recommendations():
   return render_template('posts/night-life-recommendations.html')

@old_posts.route('reacting-to-cold.html')
def reacting_to_cold():
   return render_template('posts/reacting-to-cold.html')

@old_posts.route('what-is-about-temperature-stress.html')
def what_is_about_temperature_stress():
   return render_template('posts/what-is-about-temperature-stress.html')

@old_posts.route('probiotics-and-prebiotics-crucial-for-health.html')
def probiotics_and_prebiotics_crucial_for_health():
   return render_template('posts/probiotics-and-prebiotics-crucial-for-health.html')

@old_posts.route('circadian-components-in-eating.html')
def circadian_components_in_eating():
   return render_template('posts/circadian-components-in-eating.html')

@old_posts.route('hormesis-a-little-bit-of-bad-good.html')
def hormesis_a_little_bit_of_bad_good():
   return render_template('posts/hormesis-a-little-bit-of-bad-good.html')

@old_posts.route('fasting-is-not-what-you-think.html')
def fasting_is_not_what_you_think():
   return render_template('posts/fasting-is-not-what-you-think.html')

@old_posts.route('breast-milk-for-microbiome.html')
def breast_milk_for_microbiome():
   return render_template('posts/breast-milk-for-microbiome.html')

@old_posts.route('developing-together-with-microbiome-from-birth.html')
def developing_together_with_microbiome_from_birth():
   return render_template('posts/developing-together-with-microbiome-from-birth.html')

@old_posts.route('sleep-under-alcohol.html')
def sleep_under_alcohol():
   return render_template('posts/sleep-under-alcohol.html')

@old_posts.route('fasting-nuances-ii-age-muscle-brain.html')
def fasting_nuances_ii_age_muscle_brain():
   return render_template('posts/fasting-nuances-ii-age-muscle-brain.html')

@old_posts.route('vagus-nerve.html')
def vagus_nerve():
   return render_template('posts/vagus-nerve.html')

@old_posts.route('what-is-a-temperature-anyway.html')
def what_is_a_temperature_anyway():
   return render_template('posts/what-is-a-temperature-anyway.html')

@old_posts.route('what-to-eat-on-fmd.html')
def what_to_eat_on_fmd():
   return render_template('posts/what-to-eat-on-fmd.html')

@old_posts.route('cool-sleep.html')
def cool_sleep():
   return render_template('posts/cool-sleep.html')

@old_posts.route('ghrelin-and-hunger.html')
def ghrelin_and_hunger():
   return render_template('posts/ghrelin-and-hunger.html')

@old_posts.route('do-not-stress-microbs.html')
def do_not_stress_microbs():
   return render_template('posts/do-not-stress-microbs.html')

@old_posts.route('how-to-feel-temperature.html')
def how_to_feel_temperature():
   return render_template('posts/how-to-feel-temperature.html')

@old_posts.route('what-to-eat-for-microbiome-to-thrive.html')
def what_to_eat_for_microbiome_to_thrive():
   return render_template('posts/what-to-eat-for-microbiome-to-thrive.html')

@old_posts.route('fasting-nuances-i-deficiencies.html')
def fasting_nuances_i_deficiencies():
   return render_template('posts/fasting-nuances-i-deficiencies.html')

@old_posts.route('melatonin-aka-sleep-hormone.html')
def melatonin_aka_sleep_hormone():
   return render_template('posts/melatonin-aka-sleep-hormone.html')

@old_posts.route('everyone-sleeps.html')
def everyone_sleeps():
   return render_template('posts/everyone-sleeps.html')

@old_posts.route('fat-is-good.html')
def fat_is_good():
   return render_template('posts/fat-is-good.html')

@old_posts.route('breast-milk-vs-baby-formulas.html')
def breast_milk_vs_baby_formulas():
   return render_template('posts/breast-milk-vs-baby-formulas.html')

@old_posts.route('cleaning-byproducts-during-sleep.html')
def cleaning_byproducts_during_sleep():
   return render_template('posts/cleaning-byproducts-during-sleep.html')

@old_posts.route('metabolic-flexibility.html')
def metabolic_flexibility():
   return render_template('posts/metabolic-flexibility.html')

@old_posts.route('what-destroying-microbiome-ii.html')
def what_destroying_microbiome_ii():
   return render_template('posts/what-destroying-microbiome-ii.html')

@old_posts.route('growing-in-sleep.html')
def growing_in_sleep():
   return render_template('posts/growing-in-sleep.html')

@old_posts.route('fasting-nuances-iv-toxins-release.html')
def fasting_nuances_iv_toxins_release():
   return render_template('posts/fasting-nuances-iv-toxins-release.html')

@old_posts.route('adenosine-and-how-it-bullied-by-caffeine.html')
def adenosine_and_how_it_bullied_by_caffeine():
   return render_template('posts/adenosine-and-how-it-bullied-by-caffeine.html')

@old_posts.route('mtor-to-grow-or-to-survive.html')
def mtor_to_grow_or_to_survive():
   return render_template('posts/mtor-to-grow-or-to-survive.html')

@old_posts.route('time-restricted-eating-i.html')
def time_restricted_eating_i():
   return render_template('posts/time-restricted-eating-i.html')

@old_posts.route('fasting-nuances-iii-diseases.html')
def fasting_nuances_iii_diseases():
   return render_template('posts/fasting-nuances-iii-diseases.html')

@old_posts.route('time-restricted-eating-ii.html')
def time_restricted_eating_ii():
   return render_template('posts/time-restricted-eating-ii.html')

@old_posts.route('light-brightness-discussion.html')
def light_brightness_discussion():
   return render_template('posts/light-brightness-discussion.html')

@old_posts.route('not-a-medicine-fasting.html')
def not_a_medicine_fasting():
   return render_template('posts/not-a-medicine-fasting.html')

@old_posts.route('autophagy-or-selfeating.html')
def autophagy_or_selfeating():
   return render_template('posts/autophagy-or-selfeating.html')

@old_posts.route('smart-sleep.html')
def smart_sleep():
   return render_template('posts/smart-sleep.html')

@old_posts.route('sleep-phazes-and-brain-waves.html')
def sleep_phazes_and_brain_waves():
   return render_template('posts/sleep-phazes-and-brain-waves.html')
