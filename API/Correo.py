from email.message import EmailMessage
import ssl
import smtplib

class CorreoSer:
    user = "orquestafilarmonicaud2023@gmail.com"
    password = "nfznapddjunwkhek"

    def enviarCorreo(asunto,contenido,remitente):
        em = EmailMessage()
        em['From'] = CorreoSer.user
        em['To'] = remitente
        em['Subject'] = asunto
        em.set_content(contenido)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(CorreoSer.user, CorreoSer.password)
            smtp.sendmail(CorreoSer.user, remitente, em.as_string())

            smtp.quit()

