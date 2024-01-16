from django import forms
from django.db.models.fields import Field
from django.http import request
from .models import BanqueImange, Demande, BanqueImangePhoto, BanqueRessource, Blog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Column, Div, HTML, Hidden, Layout, MultiField, Row, Submit

class BanqueImangeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'bootstrap4'
        self.helper.form_id = 'banque-image'
        self.helper.form_method='POST'
        # Tu définis la taille des labels et des champs sur la grille
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
        #HTML("""<input type='hidden' value= """ +),
        'events',
        'comments',
        'photo',
        #HTML("""<input type='' value={{created_date}} name='date' />""") ,
        HTML("""<input type='hidden' value="{{userd}}" name='user' />""") ,
        HTML("""<input name='statut' type='hidden' value='publié' />""") ,

        
        # Row(

            
        #         Column('photo', 
        #         #HTML("""<img style= 'height: 150px; width: 150px' id="previewImg" src="../static/img/transparent.png " alt="Placeholder">"""),
        #         css_class='col-md-4',
        #         ),
                
            
        # ),

            Row(
            Column( css_class='col-md-4'),
            Column(Submit('submit', 'Enregistrer'),
                    Button('cancel', 'Annuler'), css_class='col-md-4'),

            )
        )

      
    class Meta:
        model = BanqueImange
        fields = '__all__'
        labels = {
            'events': 'Renseigner l\'événement',
            'comments': 'Votre commentaire',
        }



class ImagePhotoAddForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'bootstrap4'
        self.helper.form_id = 'banque-imageAdd'
        self.helper.form_method='POST'
        # Tu définis la taille des labels et des champs sur la grille
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
        #HTML("""<input type='hidden' value= """ +),
        'eventss',
        'commentss',
        'photo',
        #HTML("""<input type='' value={{created_date}} name='date' />""") ,
        HTML("""<input type='hidden' value="{{userd}}" name='user' />""") ,
        HTML("""<input name='statut' type='hidden' value='publié' />""") ,

        
        # Row(

            
        #         Column('photo', 
        #         #HTML("""<img style= 'height: 150px; width: 150px' id="previewImg" src="../static/img/transparent.png " alt="Placeholder">"""),
        #         css_class='col-md-4',
        #         ),
                
            
        # ),

            Row(
            Column( css_class='col-md-4'),
            Column(Submit('submit', 'Enregistrer'),
                    Button('cancel', 'Annuler'), css_class='col-md-4'),

            )
        )

      
    class Meta:
        model = BanqueImangePhoto
        fields = '__all__'
        labels = {
            'eventss': 'Renseigner l\'événement',
            'commentss': 'Votre commentaire',
        }

class BanqueRessourceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'bootstrap4'
        self.helper.form_id = 'banque-imageAdd'
        self.helper.form_method='POST'
        # Tu définis la taille des labels et des champs sur la grille
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
        #HTML("""<input type='hidden' value= """ +),
        'eventsss',
        'commentsss',
        'photo',
        #HTML("""<input type='' value={{created_date}} name='date' />""") ,
        HTML("""<input type='hidden' value="{{userd}}" name='user' />""") ,
        HTML("""<input name='statut' type='hidden' value='publié' />""") ,

        
        # Row(

            
        #         Column('photo', 
        #         #HTML("""<img style= 'height: 150px; width: 150px' id="previewImg" src="../static/img/transparent.png " alt="Placeholder">"""),
        #         css_class='col-md-4',
        #         ),
                
            
        # ),

            Row(
            Column( css_class='col-md-4'),
            Column(Submit('submit', 'Enregistrer'),
                    Button('cancel', 'Annuler'), css_class='col-md-4'),

            )
        )

      
    class Meta:
        model = BanqueRessource
        fields = '__all__'
        labels = {
            'eventsss': 'Template',
            'commentsss': 'Votre commentaire',
            'photo': 'fichier',
        }

class BlogForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'bootstrap4'
        self.helper.form_id = 'banque-imageAdd'
        self.helper.form_method='POST'
        # Tu définis la taille des labels et des champs sur la grille
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
        #HTML("""<input type='hidden' value= """ +),
        'tittle',
        'auteur',
        'text',
        'photo',
        #HTML("""<input type='' value={{created_date}} name='date' />""") ,
        HTML("""<input type='hidden' value="yes" name='is_featured' />""") ,
        HTML("""<input name='statut' type='hidden' value='publié' />""") ,



            Row(
            Column( css_class='col-md-4'),
            Column(Submit('submit', 'Enregistrer'),
                    Button('cancel', 'Annuler'), css_class='col-md-4'),

            )
        )

      
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            'tittle': 'Donner un tittre',
            'auteur': 'Le nom de l\'auteur',
            'text': 'Texte',
        }





class DemandeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'bootstrap4'
        self.helper.form_id = 'demande'
        self.helper.form_method='POST'
        # Tu définis la taille des labels et des champs sur la grille
        #self.helper.label_class = 'col-md-2'
        #self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
        #HTML("""<input type='hidden' value= """ +),
        'nom',
        'email',
        'adresse',
        'telephone',
        'nbre',
        'pearson',
        'responsable',
        'comments',
        #HTML("""<input type='' value={{created_date}} name='date' />""") ,
        HTML("""<input type='hidden' value={{userd}} name='user' />""") ,
        HTML("""<input name='statut' type='hidden' value='publié' />""") ,

        
        # Row(

            
        #         Column('photo', 
        #         #HTML("""<img style= 'height: 150px; width: 150px' id="previewImg" src="../static/img/transparent.png " alt="Placeholder">"""),
        #         css_class='col-md-4',
        #         ),
                
            
        # ),

            Row(
            Column( css_class='col-md-4'),
            Column(Submit('submit', 'Envoyer'),
                    Button('cancel', 'Annuler'), css_class='col-md-4'),

            )
        )

      
    class Meta:
        model = Demande
        fields = '__all__'
        labels = {
            'nom': 'Nom et Prenom Demandeur',
            'email': 'Votre adresse email',
            'adresse': 'Votre adresse',
            'nbre': 'Le nombre de personnes envoyé',
            'pearson': 'Les noms',
            'responsable': 'Le responsable de l\'équipe',
            'comments': 'Les commentaires',
        }