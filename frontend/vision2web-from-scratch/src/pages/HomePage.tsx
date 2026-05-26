import { useState } from 'react'
import PageHeader from '../components/PageHeader'
import { healthCheck } from '../services/api'

export default function HomePage() {
  const [message, setMessage] = useState('Backend not checked yet.')

  const handleCheckApi = async () => {
    try {
      const data = await healthCheck()
      setMessage(`API connected: ${data.status}`)
    } catch (error) {
      setMessage('Backend connection failed.')
      console.error(error)
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto flex min-h-screen max-w-6xl flex-col gap-8 px-6 py-10">
        <PageHeader
          title="Screenshot to React + Tailwind"
          subtitle="Upload a desktop website screenshot, preview analysis output, and inspect generated frontend code."
        />]

        <section className="grid gap-6 lg:grid-cols-2">
          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-lg">
            <h2 className="mb-4 text-xl font-semibold">Upload Screenshot</h2>
            <div className="flex min-h-55 items-center justify-center rounded-xl border border-dashed border-slate-700 bg-slate-950 text-center text-slate-400">
              Upload area placeholder
            </div>
            <button className="mt-4 rounded-xl bg-cyan-400 px-4 py-2 font-medium text-slate-950 transition hover:bg-cyan-300">
              Analyze
            </button>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-lg">
            <h2 className="mb-4 text-xl font-semibold">Preview</h2>
            <div className="flex min-h-[220px items-center justify-center rounded-xl border border-slate-800 bg-slate-950 text-center text-slate-500">
              Preview placeholder
            </div>
          </div>
        </section>

        <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-lg">
          <h2 className="mb-4 text-xl font-semibold">Backend Connection</h2>
          <button
            onClick={handleCheckApi}
            className="rounded-xl bg-cyan-400 px-4 py-2 font-medium text-slate-950 transition hover:bg-cyan-300"
          >
            Check API
          </button>
          <p className="mt-4 text-slate-300">{message}</p>
        </section>
      </div>
    </main>
  )
}