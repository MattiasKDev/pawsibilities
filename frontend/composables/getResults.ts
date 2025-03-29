export default function (query: string) {
  return useState("results", () => {
    console.log("Fetching results for:", query);
    return [
      { name: "Alice", price: 10 },
      { name: "Bob", price: 15 },
      { name: "Charlie", price: 20 }
    ];
  });
}
