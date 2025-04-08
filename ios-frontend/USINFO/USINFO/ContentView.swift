//
//  ContentView.swift
//  USINFO
//
//  Created by Alex Jackman on 4/7/25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("USINFO")
                .font(.title)
            HStack {
                Text("United States Information & National FOundation for Transparency")
                    .font(.subheadline)
                Spacer()
                Text("Salt Lake City")
                    .font(.subheadline)
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
