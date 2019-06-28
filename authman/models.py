# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import random
import string

class Foodfacttable(models.Model):
    code = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    created_t = models.TextField(blank=True, null=True)
    created_datetime = models.TextField(blank=True, null=True)
    last_modified_t = models.TextField(blank=True, null=True)
    last_modified_datetime = models.TextField(blank=True, null=True)
    product_name = models.TextField(primary_key=True, default=''.join(random.choice(string.ascii_lowercase) for i in range(10)))
    generic_name = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    packaging = models.TextField(blank=True, null=True)
    packaging_tags = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    brands_tags = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    categories_tags = models.TextField(blank=True, null=True)
    categories_en = models.TextField(blank=True, null=True)
    origins = models.TextField(blank=True, null=True)
    origins_tags = models.TextField(blank=True, null=True)
    manufacturing_places = models.TextField(blank=True, null=True)
    manufacturing_places_tags = models.TextField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)
    labels_tags = models.TextField(blank=True, null=True)
    labels_en = models.TextField(blank=True, null=True)
    emb_codes = models.TextField(blank=True, null=True)
    emb_codes_tags = models.TextField(blank=True, null=True)
    first_packaging_code_geo = models.TextField(blank=True, null=True)
    cities = models.TextField(blank=True, null=True)
    cities_tags = models.TextField(blank=True, null=True)
    purchase_places = models.TextField(blank=True, null=True)
    stores = models.TextField(blank=True, null=True)
    countries = models.TextField(blank=True, null=True)
    countries_tags = models.TextField(blank=True, null=True)
    countries_en = models.TextField(blank=True, null=True)
    ingredients_text = models.TextField(blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)
    allergens_en = models.TextField(blank=True, null=True)
    traces = models.TextField(blank=True, null=True)
    traces_tags = models.TextField(blank=True, null=True)
    traces_en = models.TextField(blank=True, null=True)
    serving_size = models.TextField(blank=True, null=True)
    no_nutriments = models.TextField(blank=True, null=True)
    additives_n = models.TextField(blank=True, null=True)
    additives = models.TextField(blank=True, null=True)
    additives_tags = models.TextField(blank=True, null=True)
    additives_en = models.TextField(blank=True, null=True)
    ingredients_from_palm_oil_n = models.TextField(blank=True, null=True)
    ingredients_from_palm_oil = models.TextField(blank=True, null=True)
    ingredients_from_palm_oil_tags = models.TextField(blank=True, null=True)
    ingredients_that_may_be_from_palm_oil_n = models.TextField(blank=True, null=True)
    ingredients_that_may_be_from_palm_oil = models.TextField(blank=True, null=True)
    ingredients_that_may_be_from_palm_oil_tags = models.TextField(blank=True, null=True)
    nutrition_grade_uk = models.TextField(blank=True, null=True)
    nutrition_grade_fr = models.TextField(blank=True, null=True)
    pnns_groups_1 = models.TextField(blank=True, null=True)
    pnns_groups_2 = models.TextField(blank=True, null=True)
    states = models.TextField(blank=True, null=True)
    states_tags = models.TextField(blank=True, null=True)
    states_en = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    main_category_en = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    image_small_url = models.TextField(blank=True, null=True)
    energy_100g = models.TextField(blank=True, null=True)
    energy_from_fat_100g = models.TextField(db_column='energy-from-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fat_100g = models.TextField(blank=True, null=True)
    saturated_fat_100g = models.TextField(db_column='saturated-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_butyric_acid_100g = models.TextField(db_column='-butyric-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_caproic_acid_100g = models.TextField(db_column='-caproic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_caprylic_acid_100g = models.TextField(db_column='-caprylic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_capric_acid_100g = models.TextField(db_column='-capric-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_lauric_acid_100g = models.TextField(db_column='-lauric-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_myristic_acid_100g = models.TextField(db_column='-myristic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_palmitic_acid_100g = models.TextField(db_column='-palmitic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_stearic_acid_100g = models.TextField(db_column='-stearic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_arachidic_acid_100g = models.TextField(db_column='-arachidic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_behenic_acid_100g = models.TextField(db_column='-behenic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_lignoceric_acid_100g = models.TextField(db_column='-lignoceric-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_cerotic_acid_100g = models.TextField(db_column='-cerotic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_montanic_acid_100g = models.TextField(db_column='-montanic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_melissic_acid_100g = models.TextField(db_column='-melissic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    monounsaturated_fat_100g = models.TextField(db_column='monounsaturated-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polyunsaturated_fat_100g = models.TextField(db_column='polyunsaturated-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    omega_3_fat_100g = models.TextField(db_column='omega-3-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_alpha_linolenic_acid_100g = models.TextField(db_column='-alpha-linolenic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_eicosapentaenoic_acid_100g = models.TextField(db_column='-eicosapentaenoic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_docosahexaenoic_acid_100g = models.TextField(db_column='-docosahexaenoic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    omega_6_fat_100g = models.TextField(db_column='omega-6-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_linoleic_acid_100g = models.TextField(db_column='-linoleic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_arachidonic_acid_100g = models.TextField(db_column='-arachidonic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gamma_linolenic_acid_100g = models.TextField(db_column='-gamma-linolenic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dihomo_gamma_linolenic_acid_100g = models.TextField(db_column='-dihomo-gamma-linolenic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    omega_9_fat_100g = models.TextField(db_column='omega-9-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_oleic_acid_100g = models.TextField(db_column='-oleic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_elaidic_acid_100g = models.TextField(db_column='-elaidic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gondoic_acid_100g = models.TextField(db_column='-gondoic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_mead_acid_100g = models.TextField(db_column='-mead-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_erucic_acid_100g = models.TextField(db_column='-erucic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_nervonic_acid_100g = models.TextField(db_column='-nervonic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    trans_fat_100g = models.TextField(db_column='trans-fat_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cholesterol_100g = models.TextField(blank=True, null=True)
    carbohydrates_100g = models.TextField(blank=True, null=True)
    sugars_100g = models.TextField(blank=True, null=True)
    field_sucrose_100g = models.TextField(db_column='-sucrose_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_glucose_100g = models.TextField(db_column='-glucose_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_fructose_100g = models.TextField(db_column='-fructose_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_lactose_100g = models.TextField(db_column='-lactose_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_maltose_100g = models.TextField(db_column='-maltose_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_maltodextrins_100g = models.TextField(db_column='-maltodextrins_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    starch_100g = models.TextField(blank=True, null=True)
    polyols_100g = models.TextField(blank=True, null=True)
    fiber_100g = models.TextField(blank=True, null=True)
    proteins_100g = models.TextField(blank=True, null=True)
    casein_100g = models.TextField(blank=True, null=True)
    serum_proteins_100g = models.TextField(db_column='serum-proteins_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nucleotides_100g = models.TextField(blank=True, null=True)
    salt_100g = models.TextField(blank=True, null=True)
    sodium_100g = models.TextField(blank=True, null=True)
    alcohol_100g = models.TextField(blank=True, null=True)
    vitamin_a_100g = models.TextField(db_column='vitamin-a_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beta_carotene_100g = models.TextField(db_column='beta-carotene_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_d_100g = models.TextField(db_column='vitamin-d_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_e_100g = models.TextField(db_column='vitamin-e_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_k_100g = models.TextField(db_column='vitamin-k_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_c_100g = models.TextField(db_column='vitamin-c_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_b1_100g = models.TextField(db_column='vitamin-b1_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_b2_100g = models.TextField(db_column='vitamin-b2_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_pp_100g = models.TextField(db_column='vitamin-pp_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_b6_100g = models.TextField(db_column='vitamin-b6_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vitamin_b9_100g = models.TextField(db_column='vitamin-b9_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folates_100g = models.TextField(blank=True, null=True)
    vitamin_b12_100g = models.TextField(db_column='vitamin-b12_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    biotin_100g = models.TextField(blank=True, null=True)
    pantothenic_acid_100g = models.TextField(db_column='pantothenic-acid_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    silica_100g = models.TextField(blank=True, null=True)
    bicarbonate_100g = models.TextField(blank=True, null=True)
    potassium_100g = models.TextField(blank=True, null=True)
    chloride_100g = models.TextField(blank=True, null=True)
    calcium_100g = models.TextField(blank=True, null=True)
    phosphorus_100g = models.TextField(blank=True, null=True)
    iron_100g = models.TextField(blank=True, null=True)
    magnesium_100g = models.TextField(blank=True, null=True)
    zinc_100g = models.TextField(blank=True, null=True)
    copper_100g = models.TextField(blank=True, null=True)
    manganese_100g = models.TextField(blank=True, null=True)
    fluoride_100g = models.TextField(blank=True, null=True)
    selenium_100g = models.TextField(blank=True, null=True)
    chromium_100g = models.TextField(blank=True, null=True)
    molybdenum_100g = models.TextField(blank=True, null=True)
    iodine_100g = models.TextField(blank=True, null=True)
    caffeine_100g = models.TextField(blank=True, null=True)
    taurine_100g = models.TextField(blank=True, null=True)
    ph_100g = models.TextField(blank=True, null=True)
    fruits_vegetables_nuts_100g = models.TextField(db_column='fruits-vegetables-nuts_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fruits_vegetables_nuts_estimate_100g = models.TextField(db_column='fruits-vegetables-nuts-estimate_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    collagen_meat_protein_ratio_100g = models.TextField(db_column='collagen-meat-protein-ratio_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cocoa_100g = models.TextField(blank=True, null=True)
    chlorophyl_100g = models.TextField(blank=True, null=True)
    carbon_footprint_100g = models.TextField(db_column='carbon-footprint_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nutrition_score_fr_100g = models.TextField(db_column='nutrition-score-fr_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nutrition_score_uk_100g = models.TextField(db_column='nutrition-score-uk_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glycemic_index_100g = models.TextField(db_column='glycemic-index_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    water_hardness_100g = models.TextField(db_column='water-hardness_100g', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'foodfacts'
