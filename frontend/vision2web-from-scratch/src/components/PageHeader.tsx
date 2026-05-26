type PageHeaderProps = {
  title: string
  subtitle: string
}

export default function PageHeader({ title, subtitle }: PageHeaderProps) {
  return (
    <header className="space-y-3">
      <p className="text-sm uppercase tracking-[0.3em] text-cyan-300">
        Vision2Web
      </p>
      <h1 className="text-4xl font-bold tracking-tight">{title}</h1>
      <p className="max-w-2xl text-slate-300">{subtitle}</p>
    </header>
  )
}