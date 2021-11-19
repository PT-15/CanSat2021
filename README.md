# CanSat2021

Código para concurso CanSat 2021 del grupo del IES Rego de Trabe.

![logo del equipo](./logo.png)

Para configurar el arranque automático[^1]:

    sudo cp cansat.service /lib/systemd/system
    sudo chmod 644 /lib/systemd/system/cansat.service
    sudo systemctl daemon-reload
    sudo systemctl enable cansat.service
    sudo reboot

Para parar o empezar el proceso una vez encendida:

    sudo service cansat stop
    sudo service cansat start
    
[^1]: [Más información y opciones de arranque automático](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
