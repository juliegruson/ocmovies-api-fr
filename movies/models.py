from django.db import models


class Movie(models.Model):
    """Represent movie info as extracted from the IMDb database."""

    id = models.BigIntegerField('imdb title id', primary_key=True)
    title = models.CharField('movie title', max_length=255)
    original_title = models.CharField('original movie title', max_length=255)
    year = models.IntegerField('movie year')
    date_published = models.DateField('movie publishing date')
    duration = models.IntegerField('movie duration')
    description = models.TextField('movie short description', blank=True)
    long_description = models.TextField('movie long description', blank=True)
    avg_vote = models.IntegerField('average user vote')
    imdb_score = models.IntegerField('movie imdb score')
    metascore = models.IntegerField('movie metascore', null=True)
    votes = models.IntegerField('number of votes')
    budget = models.BigIntegerField('movie budget', null=True)
    budget_currency = models.CharField(
        'movie budget currency', max_length=5, null=True
    )
    usa_gross_income = models.BigIntegerField(
        'movie gross income in the usa', null=True
    )
    worldwide_gross_income = models.BigIntegerField(
        'movie gross income worldwide', null=True
    )
    reviews_from_critics = models.IntegerField(
        'number of reviews from users', null=True
    )
    image_url = models.URLField('poster image url', null=True, blank=True)
    url = models.URLField('movie imdb url')

    actors = models.ManyToManyField(
        'Contributor', through='MovieActor', related_name='movies_as_actor'
    )
    directors = models.ManyToManyField(
        'Contributor',
        through='MovieDirector',
        related_name='movies_as_director',
    )
    writers = models.ManyToManyField(
        'Contributor', through='MovieWriter', related_name='movies_as_writer'
    )
    genres = models.ManyToManyField('Genre', related_name='movies')
    countries = models.ManyToManyField('Country', related_name='movies')
    languages = models.ManyToManyField('Language', related_name='movies')
    rated = models.ForeignKey(
        'Rating', on_delete=models.SET_NULL, related_name='movies', null=True
    )
    company = models.ForeignKey(
        'Company', on_delete=models.SET_NULL, related_name='movies', null=True
    )

    def __str__(self):
        return f'{self.title} ({self.imdb_title_id})'

    @property
    def imdb_title_id(self):
        """Movie IMDB unique id."""
        return f"tt{self.id:07d}"


class Contributor(models.Model):
    """Represents a person having contributed to a movie either as actor,
    director or writer."""

    full_name = models.CharField(
        'contributor full name', max_length=200, unique=True
    )

    def __str__(self):
        return self.full_name


class MovieDirector(models.Model):
    """Represents the association between a movie and its director(s)."""

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    position = models.IntegerField('position in the directors list', null=True)


class MovieActor(models.Model):
    """Represents the association between a movie and its actors(s)."""

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    position = models.IntegerField('position in the directors list', null=True)


class MovieWriter(models.Model):
    """Represents the association between a movie and its writer(s)."""

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    position = models.IntegerField('position in the directors list', null=True)


class Genre(models.Model):
    """Represents the genre of the movie."""

    name = models.CharField('genre of the movie', max_length=200, unique=True)


class Country(models.Model):
    """Represents the country where a movie was created."""

    name = models.CharField('country name', max_length=200, unique=True)


class Language(models.Model):
    """Represents a language for a movie or its translation."""

    name = models.CharField('language name', max_length=200, unique=True)


class Rating(models.Model):
    """Represents a rating attributed to a movie."""

    name = models.CharField('rating name', max_length=200, unique=True)


class Company(models.Model):
    """Represents a production company publishing a movie."""

    name = models.CharField(
        'production company name', max_length=200, unique=True
    )
