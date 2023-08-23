export function getArray(): string {
    const data = [1, 2, 3, 5, 5]

    const dictionary = data.reduce<Record<number, number>>((acc, value, index) => {
        acc[index] = Math.max(0, Math.min(255, value))
        return acc
    }, {})

    const jsonData = JSON.stringify(dictionary)
    return jsonData
}
