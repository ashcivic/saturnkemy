/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['backend/tarefas/templates/**/*.html', // Todos os templates HTML do Django
        'backend/tarefas/static/tarefas/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        'backend/tarefas/static/tarefas/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
        'backend/sngpc/templates/**/*.html', // Todos os templates HTML do Django
        'backend/sngpc/static/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        'backend/sngpc/static/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
        'backend/core/templates/**/*.html', // Todos os templates HTML do Django
        'backend/core/static/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        'backend/core/static/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
        './tarefas/templates/**/*.html', // Todos os templates HTML do Django
        './tarefas/static/tarefas/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        './tarefas/static/tarefas/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
        './sngpc/templates/**/*.html', // Todos os templates HTML do Django
        './sngpc/static/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        './sngpc/static/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
        './core/templates/**/*.html', // Todos os templates HTML do Django
        './core/static/js/**/*.js', // Scripts estáticos onde as classes Tailwind podem ser usadas
        './core/static/css/**/*.css', // Arquivos CSS onde @apply ou classes podem ser usadas
  
  ],
  safelist: [
    'bg-blue-500',
    'text-white',
    'p-4',
],
  theme: {
    extend: {},
  },
  plugins: [],
}

