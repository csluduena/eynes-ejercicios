# Eynes Exercises

#### Recursos Utilizados (ejemplo: Google, StackOverflow, etc)
1. Documentación oficial de Python - math.pi para constante π (círculo)
2. Repaso de fórmulas básicas de geometría (área y perímetro del círculo)
3. Documentación de GitHub Actions para actualizar versiones deprecadas
4. GitHub Changelog para verificar versiones actuales de actions
5. Análisis de logs de GitHub Actions para debugging
6. Documentación oficial de Python - Listas para list comprehension anidada (matrices)
7. Python Built-in Functions - len(), range() para operaciones con dimensiones
8. Algoritmos de transposición de matrices - conceptos matemáticos fundamentales

#### Comentarios que quieras hacernos

##### ✅ Ejercicio Circle - Implementación Completa
- **Status**: Ejercicio completado exitosamente con implementación 100% funcional
- **Tests locales**: 6/6 tests pasando (pytest -v)
- **Calidad de código**: Sin errores Flake8, cumple estándares de desarrollo
- **Metodología**: Desarrollo incremental con 2 commits como especifica el instructivo

##### ✅ Ejercicio Matrix - Implementación Completa
- **Status**: Ejercicio completado exitosamente con implementación 100% funcional
- **Tests locales**: 8/8 tests pasando (pytest -v)
- **Calidad de código**: Sin errores Flake8, cumple estándares de desarrollo
- **Metodología**: Desarrollo incremental - Commit 1: casos básicos (4/8 tests), Commit 2: implementación completa (8/8 tests)
- **Técnica**: Uso de list comprehension anidada para eficiencia en transposición de matrices

##### 🔧 Diagnóstico y Resolución de Problema Técnico Crítico

**PROBLEMA IDENTIFICADO**: El template original contenía GitHub Actions con versiones deprecadas que impedían la ejecución correcta del workflow de CI/CD:
- `actions/checkout@v2` → DEPRECADA
- `actions/setup-python@v2` → DEPRECADA  
- `actions/upload-artifact@v2` → DEPRECADA

**IMPACTO**: El workflow fallaba en la fase de setup antes de ejecutar los tests, impidiendo obtener la validación automática (luz verde) del código desarrollado.

**OBJETIVO**: Resolver definitivamente este bloqueo técnico para obtener la confirmación automática de que los ejercicios cumplen todos los criterios de calidad establecidos.

**SOLUCIÓN IMPLEMENTADA**: 
- Actualización completa a versiones estables y actuales (@v4)
- Corrección de sintaxis YAML para compatibilidad
- Verificación de funcionamiento del pipeline completo de CI/CD

**RESULTADO ESPERADO**: Workflow funcional que valide automáticamente la calidad del código y permita demostrar el cumplimiento total de los requerimientos técnicos.
