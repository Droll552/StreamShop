from django.db import models

from .product import Product


class MediaProduct(Product):

    class CategoryChoices(models.TextChoices):
        LP = "lp", "LP"
        SINGLE = "single", "Single"
        FORTY_FIVE = "45", "45"
        BOXSET = "boxset", "Boxset"
        TWO_LP = "2_lp", "2 LP"

    class GenreChoices(models.TextChoices):
        BLUES = "blues", "Blues"
        BRASS_AND_MILITARY = "brass_and_military", "Brass & Military"
        CHILDREN = "children", "Children"
        CLASSICAL = "classical", "Classical"
        ELECTRONIC = "electronic", "Electronic"
        FOLK_COUNTRY = "folk_country", "Folk Country"
        FUNK_SOUL = "funk_soul", "Funk Soul"
        HIP_HOP = "hip_hop", "Hip Hop"
        JAZZ = "jazz", "Jazz"
        NON_MUSIC = "non_music", "Non Music"
        RELATHIONSHIPPOP = "relathionshippop", "Relathionshippop"
        REGGAE = "reggae", "Reggae"
        STAGE = "stage", "Stage"

    class RecordSizeChoices(models.TextChoices):
        SEVEN_INCH = "7_inch", "7''"
        TEN_INCH = "10_inch", "10''"
        TWELVE_INCH = "12_inch", "12''"

    class FormatChoices(models.TextChoices):
        VINYL = "vinyl", "Vinyl"
        CD = "cd", "CD"
        CASSETTE = "cassette", "Cassette"
        DVD = "dvd", "DVD"
        VHS = "vhs", "VHS"
        LASER_DISC = "laser_disc", "Laser Disc"
        BLURAY = "bluray", "Bluray"
        EIGHT_TRACK = "8_track", "8-Track"
        MEDIA_BOX_THIRTY_THREE = "media_box_33", "Media Box (33)"
        LARGE_BOX_THIRTY_THREE = "large_box_33", "Large Box (33)"
        MEDIA_BOX_FORTY_FIVE = "media_box_45", "Media Box (45)"
        INNER_GEN_SLEEVE = "inner_gen_sleeve", "Inner Gen Sleeve"
        INNER_TOP_SLEEVE = "inner_top_sleeve", "Inner Top Sleeve"
        OUTER_TWO_MM_SLEEVE = "outer_2mm_sleeve", "Outer 2mm Sleeve"
        OUTER_FOUR_MM_SLEEVE = "outer_4mm_sleeve", "Outer 4mm Sleeve"
        CARDBOARD_INSERTS = "cardboard_inserts", "Cardboard Inserts"
        SMALL_BUBBLE_MAILER = "small_bubble_mailer", "Small Bubble Mailer"
        LARGE_BUBBLE_MAILER = "large_bubble_mailer", "Large Bubble Mailer"

    class ConditionChoices(models.TextChoices):
        MINT_SLD = "mint_sld", "MT/SLD"
        NEAR_MINT_NEAR_MINT = "near_mint_near_mint", "NM/NM"
        NEAR_MINT_VERY_GOOD_PLUS = "near_mint_very_good_plus", "NM/VG+"
        NEAR_MINT_VERY_GOOD = "near_mint_very_good", "NM/VG"
        NEAR_MINT_VERY_GOOD_MINUS = "near_mint_very_good_minus", "NM/VG-"
        NEAR_MINT_GOOD_PLUS = "near_mint_good_plus", "NM/G+"
        NEAR_MINT_GOOD = "near_mint_good", "NM/G"
        VERY_GOOD_PLUS_NEAR_MINT = "very_good_plus_near_mint", "VG+/NM"
        VERY_GOOD_PLUS_VERY_GOOD_PLUS = "very_good_plus_very_good_plus", "VG+/VG+"
        VERY_GOOD_PLUS_VERY_GOOD = "very_good_plus_very_good", "VG+/VG"
        VERY_GOOD_PLUS_VERY_GOOD_MINUS = "very_good_plus_very_good_minus", "VG+/VG-"
        VERY_GOOD_PLUS_GOOD_PLUS = "very_good_plus_good_plus", "VG+/G+"
        VERY_GOOD_PLUS_GOOD = "very_good_plus_good", "VG+/G"
        VERY_GOOD_NEAR_MINT = "very_good_near_mint", "VG/NM"
        VERY_GOOD_VERY_GOOD_PLUS = "very_good_very_good_plus", "VG/VG+"
        VERY_GOOD_VERY_GOOD = "very_good_very_good", "VG/VG"
        VERY_GOOD_VERY_GOOD_MINUS = "very_good_very_good_minus", "VG/VG-"
        VERY_GOOD_GOOD_PLUS = "very_good_good_plus", "VG/G+"
        VERY_GOOD_GOOD = "very_good_good", "VG/G"
        GOOD_PLUS_NEAR_MINT = "good_plus_near_mint", "G+/NM"
        GOOD_PLUS_VERY_GOOD_PLUS = "good_plus_very_good_plus", "G+/VG+"
        GOOD_PLUS_VERY_GOOD = "good_plus_very_good", "G+/VG"
        GOOD_PLUS_VERY_GOOD_MINUS = "good_plus_very_good_minus", "G+/VG-"
        GOOD_PLUS_GOOD_PLUS = "good_plus_good_plus", "G+/G+"
        GOOD_PLUS_GOOD = "good_plus_good", "G+/G"
        GOOD_NEAR_MINT = "good_near_mint", "G/NM"
        GOOD_VERY_GOOD_PLUS = "good_very_good_plus", "G/VG+"
        GOOD_VERY_GOOD = "good_very_good", "G/VG"
        GOOD_VERY_GOOD_MINUS = "good_very_good_minus", "G/VG-"
        GOOD_GOOD_PLUS = "good_good_plus", "G/G+"
        GOOD_GOOD = "good_good", "G/G"

    class FeaturesChoices(models.TextChoices):
        CLUB_PRESSING = "club_pressing", "Club Pressing"
        LIMITED_PRESSING = "limited_pressing", "Limited Pressing"
        COLOR_WAX = "color_wax", "Color Wax"
        MOFI = "mofi", "MOFI"
        HALF_SPEED = "half_speed", "Half-Speed"
        OBI = "obi", "OBI"
        MISPRINT = "misprint", "Misprint"
        SHRINK = "shrink", "Shrink"
        HYPE_STICKER = "hype_sticker", "Hype Sticker"
        PROMO = "promo", "Promo"
        WHITE_LABEL_PROMO = "white_label_promo", "White Label Promo"
        SEALED = "sealed", "Sealed"
        MATCHING_45 = "matching_45", "Matching 45"
        MONO = "mono", "MONO"
        RARE_LABEL = "rare_label", "Rare Label"
        PROMO_INSERTS = "promo_inserts", "Promo Inserts"
        SAW_CUT = "saw_cut", "Saw Cut"
        SIGNED = "signed", "Signed"
        SINGLE = "single", "Single"
        RECORD_STORE_DAY = "record_store_day", "Record Store Day"
        ONE_HUNDRED_EIGHTY_GRAM = "180_gram", "180 Gram"
        ONE_HUNDRED_FIFTY_GRAM = "150_gram", "150 Gram"
        ANALOG = "analog", "Analog"
        AUTOGRAPH = "autograph", "Autograph"

    class ConditionDetailsChoices(models.TextChoices):
        SLIGHT_EDGE_SHELF_WEAR = "slight_edge_shelf_wear", "Slight Edge/Shelf Wear"
        MODERATE_EDGE_SHELF_WEAR = "moderate_edge_shelf_wear", "Moderate Edge/Shelf Wear"
        HEAVY_EDGE_SHELF_WEAR = "heavy_edge_shelf_wear", "Heavy Edge/Shelf Wear"
        CONSISTENT_SOUND_CLARITY = "consistent_sound_clarity", "Consistent Sound Clarity"
        LIGHT_SURFACE_NOISE = "light_surface_noise", "Light Surface Noise"
        MODERATE_SURFACE_NOISE = "moderate_surface_noise", "Moderate Surface Noise"
        HEAVY_SURFACE_NOISE = "heavy_surface_noise", "Heavy Surface Noise"
        OCCASIONAL_CLICKS_POPS = "occasional_clicks_pops", "Occasional Clicks Pops"
        MODERATE_CLICKS_POPS = "moderate_clicks_pops", "Moderate Clicks Pops"
        HEAVY_CLICKS_POPS = "heavy_clicks_pops", "Heavy Clicks Pops"

    artist_name = models.CharField("Artist name", max_length=25)
    album = models.CharField("Album name", max_length=25)
    label = models.CharField("Label", max_length=25, blank=True, null=True)
    category = models.CharField("Category", max_length=6, choices=CategoryChoices.choices)
    product_type = Product.ProductTypeChoices.MEDIA
    genre = models.CharField("Genre", max_length=18, choices=GenreChoices.choices, blank=True, null=True)
    condition = models.CharField("Condition", max_length=30, choices=ConditionChoices.choices)
    record_size = models.CharField("Record Size", max_length=7, choices=RecordSizeChoices.choices, blank=True,
                                   null=True)
    discogs_link = models.URLField("Discogs Link", max_length=40, blank=True, null=True)
    popsike_link = models.URLField("Popsike Link", max_length=40, blank=True, null=True)
    catalog_number = models.CharField("Cat #", max_length=20, blank=True, null=True)
    format = models.CharField("Format", max_length=30, choices=FormatChoices.choices)
    features = models.CharField("Product Features", max_length=17, choices=FeaturesChoices.choices, null=True,
                                blank=True)
    condition_details = models.CharField("Condition Details", max_length=24, choices=ConditionDetailsChoices.choices,
                                         blank=True, null=True)

    def product_name(self):
        return f'{self.artist_name}|{self.album}'

    def description(self):
        result = f"{self.press}"
        if self.press_year:
            result += f"|{self.press_year}"
        if self.label:
            result += f"|{self.label}"
        return result + f"|{self.ConditionChoices(self.condition).label}"

    def details(self):
        return f"{self.FormatChoices(self.format).label}|{self.CategoryChoices(self.category).label}"

    def __str__(self):
        return f"{self.artist_name}|{self.album}"
