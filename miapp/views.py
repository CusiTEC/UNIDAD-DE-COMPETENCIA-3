from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    mensaje = """
    <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
    <h1>EP Ingeniería de Sistemas</h1>
    <h1>Bienvenidos</h1>
    """
    return HttpResponse(mensaje)

def uc3(request): 
    mensaje = """
    <h1>Lenguaje de Programación III</h1>
    <h2>Evaluación de la Unidad de Competencia 3</h2>
    <h2>Docente: Mg. Flor Elizabeth Cerdán León</h2>
    <h2>Integrantes:</h2>
    <ul>
        <li>Cusi Osccorima Edgar Raul</li>
        <li>Granados Pretel Carlos Eduardo</li>
        <li>Laura Antezana Sebastian Timo</li>
    </ul>
    
    """
    return HttpResponse(mensaje)
 
def noticia(request): 
    mensaje = """
    <h1>Periodistas de América TV emiten pronunciamiento: No callaremos y seguiremos investigando</h1>
    <h2>El canal interrumpió su señal para referirse al secuestro de 2 periodistas de “Cuarto poder” a manos de ronderos de Cajamarca. Eduardo Quispe y Elmer Valdivieso investigaban el presunto ofrecimiento de obras en la región por parte de Yenifer Paredes, hermana de Lilia Paredes.</h2>
    <p>Este jueves 7 de julio, América Televisión cortó su señal en vivo para emitir un comunicado en respuesta al secuestro que sufrieron los periodistas de ”Cuarto poder” Eduardo Quispe y Elmer Valdivieso a manos de los ronderos del distrito de Chadín, en la región de Cajamarca. El medio periodístico reafirmó su compromiso por continuar con las investigaciones que realizan sobre el presunto ofrecimiento de obras de saneamiento por parte de Yenifer Paredes, hermana de la primera dama, Lilia Paredes, y cuñada del presidente de la República, Pedro Castillo.

“Anoche, a esta hora, se le exigió a América Televisión interrumpir su programación para defender la vida de sus periodistas. Fuimos extorsionados por un grupo de ronderos que, abusando de su rol, secuestraron a un equipo periodístico de ‘Cuarto poder’ y para mantenerlos a salvo nos obligaron a transmitir en vivo la lectura de un manifiesto que pretendía desvirtuar una denuncia periodística por corrupción. Este hecho, claramente, fue un acto de extorsión que no debe repetirse y que no avalaremos permaneciendo en silencio”, expresó el medio.

En este sentido, América hizo un llamado a que no se normalice el ataque a la prensa cuando esta se encuentra cumpliendo su labor: “En un país en el que impera el Estado de derecho y se respeta la libertad de información, la extorsión a un medio de comunicación es un delito que nos afecta a todos, que violenta nuestros derechos y libertades, y no debe ser aceptado ni normalizado. Ello solo muestra la vulnerabilidad a la que estamos sometidos todos los peruanos y no solo la prensa independiente que investiga y denuncia actos de corrupción. Como sociedad, no podemos normalizar la delincuencia y la violencia. Debemos reaccionar y reconducir nuestro país antes de que sea demasiado tarde, y defender nuestro estado libre y democrático”.</p>
    
    """
    return HttpResponse(mensaje)
