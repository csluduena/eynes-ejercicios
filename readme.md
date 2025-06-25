# Eynes Exercises

#### Recursos Utilizados (ejemplo: Google, StackOverflow, etc)
1. Documentación oficial de Python - math.pi para constante π
2. Repaso de fórmulas básicas de geometría (área y perímetro del círculo)
3. Documentación de GitHub Actions para actualizar versiones deprecadas

#### Comentarios que quieras hacernos
- Ejercicio circle completado con implementación completa
- Todos los tests pasando, código sin errores de Flake8
- **Fix técnico aplicado**: Identifiqué que GitHub Actions fallaba por versiones deprecadas de actions (upload-artifact@v2, checkout@v2, setup-python@v2). Realicé un commit adicional actualizando a versiones actuales (@v4) para obtener la luz verde en los tests automáticos.
- Los tests del código Circle funcionan correctamente tanto local como remotamente tras el fix del workflow.
