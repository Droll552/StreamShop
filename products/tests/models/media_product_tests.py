from django.test import TestCase

from products.factories import MediaProductFactory, UserFactory
from products.models import MediaProduct, Product


class MediaProductTests(TestCase):
    def setUp(self):
        self.artist_name = "Artist"
        self.album = "Album"
        self.label = "Label"
        self.category = MediaProduct.CategoryChoices.BOXSET
        self.genre = MediaProduct.GenreChoices.BLUES
        self.condition = MediaProduct.ConditionChoices.GOOD_GOOD
        self.record_size = MediaProduct.RecordSizeChoices.SEVEN_INCH
        self.discogs_link = "https://example.com/"
        self.popsike_link = "https://example.com/"
        self.catalog_number = "number"
        self.format = MediaProduct.FormatChoices.BLURAY
        self.features = MediaProduct.FeaturesChoices.COLOR_WAX
        self.condition_details = MediaProduct.ConditionDetailsChoices.HEAVY_CLICKS_POPS
        self.user = UserFactory()
        self.asking_price = 1234.56
        self.press = Product.PressTypeChoices.ORIGINAL

        self.media_product = MediaProductFactory(
            artist_name=self.artist_name,
            album=self.album,
            label=self.label,
            category=self.category,
            genre=self.genre,
            condition=self.condition,
            record_size=self.record_size,
            discogs_link=self.discogs_link,
            popsike_link=self.popsike_link,
            catalog_number=self.catalog_number,
            format=self.format,
            features=self.features,
            condition_details=self.condition_details,
            user=self.user,
            press=self.press,
        )

    # fields

    def test_it_has_artist_name_field(self):
        self.assertEqual(self.artist_name, self.media_product.artist_name)
        self.assertEqual("Artist name", self.media_product._meta.get_field("artist_name").verbose_name)

    def test_it_has_album_field(self):
        self.assertEqual(self.album, self.media_product.album)
        self.assertEqual("Album name", self.media_product._meta.get_field("album").verbose_name)

    def test_it_has_label_field(self):
        self.assertEqual(self.label, self.media_product.label)
        self.assertEqual("Label", self.media_product._meta.get_field("label").verbose_name)

    def test_it_has_category_field(self):
        self.assertEqual(self.category, self.media_product.category)
        self.assertEqual("Category", self.media_product._meta.get_field("category").verbose_name)

    def test_it_has_genre_field(self):
        self.assertEqual(self.genre, self.media_product.genre)
        self.assertEqual("Genre", self.media_product._meta.get_field("genre").verbose_name)

    def test_it_has_condition_field(self):
        self.assertEqual(self.condition, self.media_product.condition)
        self.assertEqual("Condition", self.media_product._meta.get_field("condition").verbose_name)

    def test_it_has_record_size_field(self):
        self.assertEqual(self.record_size, self.media_product.record_size)
        self.assertEqual("Record Size", self.media_product._meta.get_field("record_size").verbose_name)

    def test_it_has_discogs_link_field(self):
        self.assertEqual(self.discogs_link, self.media_product.discogs_link)
        self.assertEqual("Discogs Link", self.media_product._meta.get_field("discogs_link").verbose_name)

    def test_it_has_popsike_link_field(self):
        self.assertEqual(self.popsike_link, self.media_product.popsike_link)
        self.assertEqual("Popsike Link", self.media_product._meta.get_field("popsike_link").verbose_name)

    def test_it_has_catalog_number_field(self):
        self.assertEqual(self.catalog_number, self.media_product.catalog_number)
        self.assertEqual("Cat #", self.media_product._meta.get_field("catalog_number").verbose_name)

    def test_it_has_format_field(self):
        self.assertEqual(self.format, self.media_product.format)
        self.assertEqual("Format", self.media_product._meta.get_field("format").verbose_name)

    def it_has_features_field(self):
        self.assertEqual(self.features, self.media_product.features)
        self.assertEqual("Product Features", self.media_product._meta.get_field("features").verbose_name)

    def it_has_condition_details_field(self):
        self.assertEqual(self.condition_details, self.media_product.condition_details)
        self.assertEqual("Condition Details", self.media_product._meta.get_field("condition_details"))

    # methods

    def test_product_name_method(self):
        self.assertEqual(f'{self.artist_name}|{self.album}', self.media_product.product_name())

    def test_description_method_without_press_year_and_label(self):
        media_product = MediaProductFactory(press="OG", condition=MediaProduct.ConditionChoices.GOOD_GOOD)
        self.assertEqual(f'OG|G/G', media_product.description())

    def test_description_method_with_press_year(self):
        media_product = MediaProductFactory(press="OG", condition="good_good", press_year=2000)
        self.assertEqual(f'OG|2000|G/G', media_product.description())

    def test_description_method_with_label(self):
        media_product = MediaProductFactory(press="OG", condition="good_good", label="label")
        self.assertEqual(f'OG|label|G/G', media_product.description())

    def test_description_method_with_press_year_and_label(self):
        media_product = MediaProductFactory(press="OG", condition="good_good", press_year=2000, label="label")
        self.assertEqual(f'OG|2000|label|G/G', media_product.description())

    def test_details_method(self):
        self.assertEqual(f'{self.format.label}|{self.category.label}', self.media_product.details())

    def test_string_representation(self):
        self.assertEqual(f'{self.artist_name}|{self.album}', str(self.media_product))
